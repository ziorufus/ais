import argparse
import json
import re
import sys
from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Any


@dataclass
class LocatedAnnotation:
    text: str
    label: str
    norm_text: str
    start: int
    end: int
    match_count: int


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Evaluate predicted span annotations against gold annotations using "
            "character-level overlap on the original text."
        )
    )
    parser.add_argument("--gold", help="Path to the gold JSON file.")
    parser.add_argument("--pred", help="Path to the predictions JSON file.")
    parser.add_argument("--text-file", help="Path to the original text file.")
    parser.add_argument(
        "--input-folder",
        help="Folder containing prediction files (*.txt). Searched recursively.",
    )
    parser.add_argument(
        "--gold-folder",
        help="Folder containing gold files with the same filename. Searched recursively.",
    )
    parser.add_argument(
        "--text-folder",
        help="Folder containing original text files with the same filename. Searched recursively.",
    )
    parser.add_argument(
        "--case-sensitive",
        action="store_true",
        help="Keep case distinctions when matching spans. Default: disabled.",
    )
    parser.add_argument(
        "--keep-non-alnum",
        action="store_true",
        help=(
            "Keep punctuation and spaces when matching spans. "
            "Default: ignore non-alphanumeric characters."
        ),
    )
    parser.add_argument(
        "--show-details",
        action="store_true",
        help="Print unresolved or ambiguous annotations.",
    )
    args = parser.parse_args()

    single_mode = bool(args.gold or args.pred or args.text_file)
    batch_mode = bool(args.input_folder or args.gold_folder or args.text_folder)

    if single_mode and batch_mode:
        parser.error("Use either single-file mode (--gold/--pred/--text-file) or folder mode (--input-folder/--gold-folder/--text-folder)")
    if not single_mode and not batch_mode:
        parser.error("Missing arguments. Use either single-file mode or folder mode.")
    if single_mode and not (args.gold and args.pred and args.text_file):
        parser.error("Single-file mode requires --gold, --pred, and --text-file")
    if batch_mode and not (args.input_folder and args.gold_folder and args.text_folder):
        parser.error("Folder mode requires --input-folder, --gold-folder, and --text-folder")

    return args


def read_text(path: str | Path) -> str:
    return Path(path).read_text(encoding="utf-8")


def load_json_like(path: str | Path) -> Any:
    raw = read_text(path).strip()

    try:
        return json.loads(raw)
    except json.JSONDecodeError:
        pass

    fenced_blocks = re.findall(r"```(?:json)?\s*(.*?)```", raw, flags=re.DOTALL | re.IGNORECASE)
    for block in fenced_blocks:
        block = block.strip()
        try:
            return json.loads(block)
        except json.JSONDecodeError:
            continue

    start = min((idx for idx in (raw.find("["), raw.find("{")) if idx != -1), default=-1)
    if start != -1:
        for end in range(len(raw), start, -1):
            candidate = raw[start:end].strip()
            try:
                return json.loads(candidate)
            except json.JSONDecodeError:
                continue

    raise ValueError(f"Could not parse JSON content from {path}")


def unwrap_annotations(data: Any) -> list[dict[str, Any]]:
    if isinstance(data, list):
        annotations = data
    elif isinstance(data, dict):
        for key in ("annotations", "items", "data", "spans", "events"):
            if key in data and isinstance(data[key], list):
                annotations = data[key]
                break
        else:
            raise ValueError("JSON must be a list or contain one of: annotations, items, data, spans")
    else:
        raise ValueError("Unsupported JSON structure")

    cleaned: list[dict[str, Any]] = []
    for idx, item in enumerate(annotations):
        if not isinstance(item, dict):
            raise ValueError(f"Annotation #{idx} is not an object")

        text = item.get("text")
        label = item.get("type", item.get("label"))
        if not isinstance(text, str) or not text.strip():
            raise ValueError(f"Annotation #{idx} has missing/empty 'text'")
        if not isinstance(label, str) or not label.strip():
            raise ValueError(f"Annotation #{idx} has missing/empty 'type'/'label'")

        cleaned.append({"text": text, "label": label})

    return cleaned


def normalize_text(text: str, keep_non_alnum: bool, case_sensitive: bool) -> str:
    chars: list[str] = []
    for char in text:
        if keep_non_alnum or char.isalnum():
            chars.append(char if case_sensitive else char.casefold())
    return "".join(chars)


def find_all_occurrences(haystack: str, needle: str) -> list[tuple[int, int]]:
    positions: list[tuple[int, int]] = []
    if not needle:
        return positions

    start = 0
    while True:
        idx = haystack.find(needle, start)
        if idx == -1:
            break
        positions.append((idx, idx + len(needle)))
        start = idx + 1
    return positions


def locate_annotations(
    annotations: list[dict[str, Any]],
    normalized_text: str,
    keep_non_alnum: bool,
    case_sensitive: bool,
) -> tuple[list[LocatedAnnotation], list[dict[str, Any]], list[dict[str, Any]]]:
    located: list[LocatedAnnotation] = []
    unresolved: list[dict[str, Any]] = []
    ambiguous: list[dict[str, Any]] = []

    for idx, item in enumerate(annotations):
        norm_span = normalize_text(item["text"], keep_non_alnum, case_sensitive)
        if not norm_span:
            unresolved.append(
                {
                    "index": idx,
                    "label": item["label"],
                    "text": item["text"],
                    "reason": "empty after normalization",
                }
            )
            continue

        matches = find_all_occurrences(normalized_text, norm_span)
        if not matches:
            unresolved.append(
                {
                    "index": idx,
                    "label": item["label"],
                    "text": item["text"],
                    "reason": "span not found in original text",
                }
            )
            continue

        if len(matches) > 1:
            ambiguous.append(
                {
                    "index": idx,
                    "label": item["label"],
                    "text": item["text"],
                    "matches": len(matches),
                    "chosen_span": [matches[0][0], matches[0][1]],
                }
            )

        located.append(
            LocatedAnnotation(
                text=item["text"],
                label=item["label"],
                norm_text=norm_span,
                start=matches[0][0],
                end=matches[0][1],
                match_count=len(matches),
            )
        )

    return located, unresolved, ambiguous


def build_label_coverage(annotations: list[LocatedAnnotation]) -> dict[str, Counter[int]]:
    coverage: dict[str, Counter[int]] = defaultdict(Counter)
    for annotation in annotations:
        for pos in range(annotation.start, annotation.end):
            coverage[annotation.label][pos] += 1
    return coverage


def score_coverages(
    gold_coverage: dict[str, Counter[int]],
    pred_coverage: dict[str, Counter[int]],
) -> dict[str, Any]:
    labels = sorted(set(gold_coverage) | set(pred_coverage))
    per_label: dict[str, dict[str, float]] = {}

    total_gold = 0
    total_pred = 0
    total_tp = 0

    for label in labels:
        gold_counter = gold_coverage.get(label, Counter())
        pred_counter = pred_coverage.get(label, Counter())

        gold_count = sum(gold_counter.values())
        pred_count = sum(pred_counter.values())
        tp = sum(min(gold_counter[pos], pred_counter[pos]) for pos in set(gold_counter) | set(pred_counter))

        precision = tp / pred_count if pred_count else 0.0
        recall = tp / gold_count if gold_count else 0.0
        f1 = (2 * precision * recall / (precision + recall)) if (precision + recall) else 0.0

        per_label[label] = {
            "gold_chars": gold_count,
            "pred_chars": pred_count,
            "matched_chars": tp,
            "precision": precision,
            "recall": recall,
            "f1": f1,
        }

        total_gold += gold_count
        total_pred += pred_count
        total_tp += tp

    micro_precision = total_tp / total_pred if total_pred else 0.0
    micro_recall = total_tp / total_gold if total_gold else 0.0
    micro_f1 = (
        2 * micro_precision * micro_recall / (micro_precision + micro_recall)
        if (micro_precision + micro_recall)
        else 0.0
    )

    return {
        "micro": {
            "gold_chars": total_gold,
            "pred_chars": total_pred,
            "matched_chars": total_tp,
            "precision": micro_precision,
            "recall": micro_recall,
            "f1": micro_f1,
        },
        "per_label": per_label,
    }


def format_pct(value: float) -> str:
    return f"{value * 100:.2f}%"


def evaluate_single_file(
    gold_path: str | Path,
    pred_path: str | Path,
    text_path: str | Path,
    *,
    case_sensitive: bool,
    keep_non_alnum: bool,
) -> dict[str, Any]:
    original_text = read_text(text_path)
    normalized_text = normalize_text(
        original_text,
        keep_non_alnum=keep_non_alnum,
        case_sensitive=case_sensitive,
    )
    if not normalized_text:
        raise ValueError(f"The original text is empty after normalization: {text_path}")

    gold_annotations = unwrap_annotations(load_json_like(gold_path))
    pred_annotations = unwrap_annotations(load_json_like(pred_path))

    gold_located, gold_unresolved, gold_ambiguous = locate_annotations(
        gold_annotations,
        normalized_text,
        keep_non_alnum=keep_non_alnum,
        case_sensitive=case_sensitive,
    )
    pred_located, pred_unresolved, pred_ambiguous = locate_annotations(
        pred_annotations,
        normalized_text,
        keep_non_alnum=keep_non_alnum,
        case_sensitive=case_sensitive,
    )

    scores = score_coverages(
        build_label_coverage(gold_located),
        build_label_coverage(pred_located),
    )

    return {
        "gold_path": str(gold_path),
        "pred_path": str(pred_path),
        "text_path": str(text_path),
        "gold_annotations": gold_annotations,
        "pred_annotations": pred_annotations,
        "gold_located": gold_located,
        "pred_located": pred_located,
        "gold_unresolved": gold_unresolved,
        "pred_unresolved": pred_unresolved,
        "gold_ambiguous": gold_ambiguous,
        "pred_ambiguous": pred_ambiguous,
        "scores": scores,
    }


def print_single_result(result: dict[str, Any], args: argparse.Namespace) -> None:
    micro = result["scores"]["micro"]

    print("Evaluation settings")
    print(f"  Text file: {result['text_path']}")
    print(f"  Gold file: {result['gold_path']}")
    print(f"  Pred file: {result['pred_path']}")
    print(f"  Case sensitive: {args.case_sensitive}")
    print(f"  Keep non-alnum: {args.keep_non_alnum}")
    print()

    print("Span resolution")
    print(f"  Gold annotations: {len(result['gold_annotations'])}")
    print(f"  Gold located: {len(result['gold_located'])}")
    print(f"  Gold unresolved: {len(result['gold_unresolved'])}")
    print(f"  Gold ambiguous: {len(result['gold_ambiguous'])}")
    print(f"  Pred annotations: {len(result['pred_annotations'])}")
    print(f"  Pred located: {len(result['pred_located'])}")
    print(f"  Pred unresolved: {len(result['pred_unresolved'])}")
    print(f"  Pred ambiguous: {len(result['pred_ambiguous'])}")
    print()

    print("Micro scores")
    print(f"  Precision: {format_pct(micro['precision'])}")
    print(f"  Recall: {format_pct(micro['recall'])}")
    print(f"  F1: {format_pct(micro['f1'])}")
    print(f"  Matched chars: {micro['matched_chars']}")
    print(f"  Gold chars: {micro['gold_chars']}")
    print(f"  Pred chars: {micro['pred_chars']}")
    print()

    print("Per-label scores")
    for label, metrics in result["scores"]["per_label"].items():
        print(
            f"  {label}: "
            f"P={format_pct(metrics['precision'])} "
            f"R={format_pct(metrics['recall'])} "
            f"F1={format_pct(metrics['f1'])} "
            f"(matched={metrics['matched_chars']}, gold={metrics['gold_chars']}, pred={metrics['pred_chars']})"
        )

    if args.show_details and (
        result["gold_unresolved"]
        or result["pred_unresolved"]
        or result["gold_ambiguous"]
        or result["pred_ambiguous"]
    ):
        print()
        print("Details")
        for name, items in (
            ("Gold unresolved", result["gold_unresolved"]),
            ("Pred unresolved", result["pred_unresolved"]),
            ("Gold ambiguous", result["gold_ambiguous"]),
            ("Pred ambiguous", result["pred_ambiguous"]),
        ):
            if not items:
                continue
            print(f"  {name}:")
            for item in items:
                print(f"    {json.dumps(item, ensure_ascii=False)}")

    summary = {
        "micro": {
            "precision": micro["precision"],
            "recall": micro["recall"],
            "f1": micro["f1"],
            "matched_chars": micro["matched_chars"],
            "gold_chars": micro["gold_chars"],
            "pred_chars": micro["pred_chars"],
        },
        "per_label": result["scores"]["per_label"],
        "resolution": {
            "gold_total": len(result["gold_annotations"]),
            "gold_located": len(result["gold_located"]),
            "gold_unresolved": len(result["gold_unresolved"]),
            "gold_ambiguous": len(result["gold_ambiguous"]),
            "pred_total": len(result["pred_annotations"]),
            "pred_located": len(result["pred_located"]),
            "pred_unresolved": len(result["pred_unresolved"]),
            "pred_ambiguous": len(result["pred_ambiguous"]),
        },
    }

    print()
    print("JSON summary")
    print(json.dumps(summary, indent=2, ensure_ascii=False))


def find_single_match(base_folder: str | Path, filename: str) -> Path:
    matches = sorted(path for path in Path(base_folder).rglob(filename) if path.is_file())
    if not matches:
        raise FileNotFoundError(f"Could not find {filename} under {base_folder}")
    if len(matches) > 1:
        raise ValueError(
            f"Found multiple matches for {filename} under {base_folder}: "
            + ", ".join(str(match) for match in matches)
        )
    return matches[0]


def evaluate_folder(args: argparse.Namespace) -> None:
    pred_files = sorted(path for path in Path(args.input_folder).rglob("*.txt") if path.is_file())
    if not pred_files:
        raise FileNotFoundError(f"No *.txt files found under {args.input_folder}")

    per_label_totals: dict[str, dict[str, int]] = defaultdict(
        lambda: {"gold_chars": 0, "pred_chars": 0, "matched_chars": 0}
    )
    file_summaries: list[dict[str, Any]] = []
    total_gold_annotations = 0
    total_pred_annotations = 0
    total_gold_located = 0
    total_pred_located = 0
    total_gold_unresolved = 0
    total_pred_unresolved = 0
    total_gold_ambiguous = 0
    total_pred_ambiguous = 0
    total_gold_chars = 0
    total_pred_chars = 0
    total_matched_chars = 0

    for pred_path in pred_files:
        filename = pred_path.name
        gold_path = find_single_match(args.gold_folder, filename)
        text_path = find_single_match(args.text_folder, filename)

        result = evaluate_single_file(
            gold_path=gold_path,
            pred_path=pred_path,
            text_path=text_path,
            case_sensitive=args.case_sensitive,
            keep_non_alnum=args.keep_non_alnum,
        )

        total_gold_annotations += len(result["gold_annotations"])
        total_pred_annotations += len(result["pred_annotations"])
        total_gold_located += len(result["gold_located"])
        total_pred_located += len(result["pred_located"])
        total_gold_unresolved += len(result["gold_unresolved"])
        total_pred_unresolved += len(result["pred_unresolved"])
        total_gold_ambiguous += len(result["gold_ambiguous"])
        total_pred_ambiguous += len(result["pred_ambiguous"])
        total_gold_chars += result["scores"]["micro"]["gold_chars"]
        total_pred_chars += result["scores"]["micro"]["pred_chars"]
        total_matched_chars += result["scores"]["micro"]["matched_chars"]

        for label, metrics in result["scores"]["per_label"].items():
            per_label_totals[label]["gold_chars"] += metrics["gold_chars"]
            per_label_totals[label]["pred_chars"] += metrics["pred_chars"]
            per_label_totals[label]["matched_chars"] += metrics["matched_chars"]

        file_summaries.append(
            {
                "file": filename,
                "pred_path": str(pred_path),
                "gold_path": str(gold_path),
                "text_path": str(text_path),
                "micro": result["scores"]["micro"],
            }
        )

    per_label_scores: dict[str, dict[str, float]] = {}
    for label in sorted(per_label_totals):
        gold_chars = per_label_totals[label]["gold_chars"]
        pred_chars = per_label_totals[label]["pred_chars"]
        matched_chars = per_label_totals[label]["matched_chars"]
        precision = matched_chars / pred_chars if pred_chars else 0.0
        recall = matched_chars / gold_chars if gold_chars else 0.0
        f1 = (2 * precision * recall / (precision + recall)) if (precision + recall) else 0.0
        per_label_scores[label] = {
            "gold_chars": gold_chars,
            "pred_chars": pred_chars,
            "matched_chars": matched_chars,
            "precision": precision,
            "recall": recall,
            "f1": f1,
        }

    micro_precision = total_matched_chars / total_pred_chars if total_pred_chars else 0.0
    micro_recall = total_matched_chars / total_gold_chars if total_gold_chars else 0.0
    micro_f1 = (
        2 * micro_precision * micro_recall / (micro_precision + micro_recall)
        if (micro_precision + micro_recall)
        else 0.0
    )
    micro = {
        "gold_chars": total_gold_chars,
        "pred_chars": total_pred_chars,
        "matched_chars": total_matched_chars,
        "precision": micro_precision,
        "recall": micro_recall,
        "f1": micro_f1,
    }

    print("Evaluation settings")
    print(f"  Input folder: {args.input_folder}")
    print(f"  Gold folder: {args.gold_folder}")
    print(f"  Text folder: {args.text_folder}")
    print(f"  Files evaluated: {len(file_summaries)}")
    print(f"  Case sensitive: {args.case_sensitive}")
    print(f"  Keep non-alnum: {args.keep_non_alnum}")
    print()

    print("Global span resolution")
    print(f"  Gold annotations: {total_gold_annotations}")
    print(f"  Gold located: {total_gold_located}")
    print(f"  Gold unresolved: {total_gold_unresolved}")
    print(f"  Gold ambiguous: {total_gold_ambiguous}")
    print(f"  Pred annotations: {total_pred_annotations}")
    print(f"  Pred located: {total_pred_located}")
    print(f"  Pred unresolved: {total_pred_unresolved}")
    print(f"  Pred ambiguous: {total_pred_ambiguous}")
    print()

    print("Global micro scores")
    print(f"  Precision: {format_pct(micro['precision'])}")
    print(f"  Recall: {format_pct(micro['recall'])}")
    print(f"  F1: {format_pct(micro['f1'])}")
    print(f"  Matched chars: {micro['matched_chars']}")
    print(f"  Gold chars: {micro['gold_chars']}")
    print(f"  Pred chars: {micro['pred_chars']}")
    print()

    print("Global per-label scores")
    for label, metrics in per_label_scores.items():
        print(
            f"  {label}: "
            f"P={format_pct(metrics['precision'])} "
            f"R={format_pct(metrics['recall'])} "
            f"F1={format_pct(metrics['f1'])} "
            f"(matched={metrics['matched_chars']}, gold={metrics['gold_chars']}, pred={metrics['pred_chars']})"
        )

    summary = {
        "micro": micro,
        "per_label": per_label_scores,
        "resolution": {
            "gold_total": total_gold_annotations,
            "gold_located": total_gold_located,
            "gold_unresolved": total_gold_unresolved,
            "gold_ambiguous": total_gold_ambiguous,
            "pred_total": total_pred_annotations,
            "pred_located": total_pred_located,
            "pred_unresolved": total_pred_unresolved,
            "pred_ambiguous": total_pred_ambiguous,
        },
        "files": file_summaries,
    }

    print()
    print("JSON summary")
    print(json.dumps(summary, indent=2, ensure_ascii=False))


def main() -> int:
    args = parse_args()

    if args.input_folder:
        evaluate_folder(args)
        return 0

    result = evaluate_single_file(
        gold_path=args.gold,
        pred_path=args.pred,
        text_path=args.text_file,
        case_sensitive=args.case_sensitive,
        keep_non_alnum=args.keep_non_alnum,
    )
    print_single_result(result, args)

    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"Error: {exc}", file=sys.stderr)
        raise
