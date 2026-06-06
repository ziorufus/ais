from pathlib import Path
from webanno_tsv import webanno_tsv_read_file
import json

TRAIN_LIST = [
    "P2_O2.txt",
    "P2_O1.txt",
    "P4_W1.txt",
    "P4_W2.txt",
    "P8_W2.txt",
    "P4_O1.txt",
    "P8_O2.txt",
    "P10_W2.txt",
    "P1_O2.txt",
    "P3_W2.txt",
    "P1_O1.txt",
    "P3_O1.txt",
    "P1_W1.txt",
    "P5_W2.txt",
    "P5_W1.txt",
    "P7_O2.txt",
    "P5_O2.txt",
    "P7_W1.txt",
    "P7_W2.txt",
    "P9_O1.txt",
]
TEST_LIST = [
    "P2_W2.txt",
    "P2_W1.txt",
    "P6_O2.txt",
    "P8_W1.txt",
    "P6_O1.txt",
    "P8_O1.txt",
    "P6_W2.txt",
    "P4_O2.txt",
    "P6_W1.txt",
    "P3_W1.txt",
    "P10_W1.txt",
    "P10_O2.txt",
    "P1_W2.txt",
    "P10_O1.txt",
    "P3_O2.txt",
    "P9_W2.txt",
    "P7_O1.txt",
    "P9_W1.txt",
    "P9_O2.txt",
    "P5_O1.txt",
]

FOLDER = Path("annotation")
GOLD_FILE = "beatricebozzetto.tsv"
OUTPUT_FOLDER = Path("txt_files")
GOLD_FOLDER = Path("gold_files")

ALL_FILES = TRAIN_LIST + TEST_LIST


def export_txt_files() -> None:
    OUTPUT_FOLDER.mkdir(parents=True, exist_ok=True)
    GOLD_FOLDER.mkdir(parents=True, exist_ok=True)

    for folder_name in ALL_FILES:
        tsv_path = FOLDER / folder_name / GOLD_FILE
        output_path = OUTPUT_FOLDER / folder_name
        gold_path = GOLD_FOLDER / folder_name

        if not tsv_path.is_file():
            raise FileNotFoundError(f"Gold file not found: {tsv_path}")

        document = webanno_tsv_read_file(tsv_path)
        output_path.write_text(document.text, encoding="utf-8")
        print(f"Saved {output_path}")

        annotations = []
        for annotation in document.annotations:
            annotations.append({"text": annotation.text, "type": annotation.layer.replace("webanno.custom.", "")})

        gold_path.write_text(json.dumps(annotations, indent=2, ensure_ascii=False), encoding="utf-8")
        print(f"Saved {gold_path}")


if __name__ == "__main__":
    export_txt_files()
