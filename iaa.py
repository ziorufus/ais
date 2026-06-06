import json
import itertools
from collections import defaultdict
from typing import Dict, Tuple, List, Set, Any
from pathlib import Path
from typing import List
from webanno_tsv import webanno_tsv_read_file, Document

DATA_FOLDER = "annotation"
REQUIRED_FILES = {"martinavacondio.tsv", "beatricebozzetto.tsv"}

def jaccard_distance(a: Set[int], b: Set[int]) -> float:
    """1 - Jaccard similarity. If both empty, distance is 0 (units with all-empty are skipped anyway)."""
    if not a and not b:
        return 0.0
    return 1.0 - (len(a & b) / len(a | b))


def parse_units(data: dict) -> Tuple[
    Dict[Tuple[str, str], Dict[str, Set[int]]], List[str], List[str]
]:
    """
    Convert input JSON to units keyed by (doc_id, label) -> {annotator: set(tokens)}.
    If an annotator has multiple spans for a label in a doc, we union the tokens.
    """
    units: Dict[Tuple[str, str], Dict[str, Set[int]]] = {}
    all_annotators: Set[str] = set()
    all_labels: Set[str] = set()

    # collect annotators and labels
    for doc_id, doc_data in data.items():
        for ann_id, spans in doc_data.items():
            all_annotators.add(ann_id)
            for s in spans:
                all_labels.add(s["label"])

    all_annotators = sorted(all_annotators)
    all_labels = sorted(all_labels)

    # build units
    for doc_id, doc_data in data.items():
        # initialize all labels for all annotators as empty
        for label in all_labels:
            units[(doc_id, label)] = {ann: set() for ann in all_annotators}

        for ann_id, spans in doc_data.items():
            by_label = defaultdict(set)
            for s in spans:
                by_label[s["label"]].update(s["tokens"])
            for label, tokset in by_label.items():
                units[(doc_id, label)][ann_id] = tokset

    return units, all_annotators, all_labels


def krippendorff_alpha_from_units(
    units: Dict[Tuple[str, str], Dict[str, Set[int]]],
    annotators: List[str],
    unit_filter=None,
) -> float:
    """
    Krippendorff's alpha on set-valued data using Jaccard distance.
    units: (doc_id,label)->{annotator->set(tokens)}
    unit_filter: optional callable(unit_key)->bool to restrict units (e.g., per label)
    """
    # select units
    selected = []
    for ukey, ann_map in units.items():
        if unit_filter is not None and not unit_filter(ukey):
            continue
        # skip non-informative units: all annotators empty
        if any(ann_map[a] for a in annotators):
            selected.append((ukey, ann_map))

    if not selected:
        return float("nan")

    # Observed disagreement Do
    Do_num = 0.0
    Do_den = 0
    for _, ann_map in selected:
        vals = [ann_map[a] for a in annotators]
        pairs = list(itertools.combinations(range(len(vals)), 2))
        if not pairs:
            continue
        for i, j in pairs:
            Do_num += jaccard_distance(vals[i], vals[j])
        Do_den += len(pairs)

    if Do_den == 0:
        return float("nan")

    Do = Do_num / Do_den

    # Expected disagreement De (pool all values across selected units)
    pool = []
    for _, ann_map in selected:
        for a in annotators:
            pool.append(ann_map[a])

    if len(pool) < 2:
        return float("nan")

    De_num = 0.0
    De_den = 0
    for i in range(len(pool)):
        for j in range(i + 1, len(pool)):
            De_num += jaccard_distance(pool[i], pool[j])
            De_den += 1
    De = De_num / De_den

    if De == 0:
        return 1.0 if Do == 0 else float("nan")

    return 1.0 - (Do / De)


def krippendorff_alpha_jaccard_global_and_per_label(data: dict) -> Dict[str, Any]:
    """
    Returns:
      {
        "alpha_global": float,
        "alpha_per_label": {label: float, ...},
        "labels": [...],
        "annotators": [...]
      }
    """
    units, annotators, labels = parse_units(data)

    alpha_global = krippendorff_alpha_from_units(units, annotators)

    alpha_per_label = {}
    for label in labels:
        alpha_per_label[label] = krippendorff_alpha_from_units(
            units, annotators, unit_filter=lambda ukey, lab=label: ukey[1] == lab
        )

    return {
        "alpha_global": alpha_global,
        "alpha_per_label": alpha_per_label,
        "labels": labels,
        "annotators": annotators,
    }

def find_folders_with_files(start_path: str | Path) -> List[Path]:
    start = Path(start_path).expanduser().resolve()
    if not start.exists():
        raise FileNotFoundError(f"Start path does not exist: {start}")
    if not start.is_dir():
        raise NotADirectoryError(f"Start path is not a directory: {start}")

    matching: List[Path] = []

    # Iterate over all directories (including nested ones)
    for folder in [start] + [p for p in start.rglob("*") if p.is_dir()]:
        names_in_folder = {p.name for p in folder.iterdir() if p.is_file()}
        if REQUIRED_FILES.issubset(names_in_folder):
            matching.append(folder)

    return matching


if __name__ == "__main__":

    # Load data
    folders = find_folders_with_files(DATA_FOLDER)
    folder_dict = {}
    for folder in folders:
        folder_dict[folder] = {}
        for annotator in REQUIRED_FILES:
            folder_dict[folder][annotator] = []
            tsv_file = folder / annotator
            doc = webanno_tsv_read_file(tsv_file)

            for annotation in doc.annotations:
                new_annotation = {"label": annotation.layer, "tokens": []}
                for token in annotation.tokens:
                    new_annotation['tokens'].append(f"{token.sentence_idx}-{token.idx}")
                print(folder.name, annotator, new_annotation)
                folder_dict[folder][annotator].append(new_annotation)

    res = krippendorff_alpha_jaccard_global_and_per_label(folder_dict)

    print("Annotators:", res["annotators"])
    print("Labels:", res["labels"])
    print("Alpha (global):", res["alpha_global"])
    print("Alpha (per label):")
    for lab, a in res["alpha_per_label"].items():
        print(f"  {lab}: {a}")
