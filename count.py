from pathlib import Path
from typing import List
from webanno_tsv import webanno_tsv_read_file, Document
import pandas as pd
import openpyxl

DATA_FOLDER = "annotation"
REQUIRED_FILES = {"beatricebozzetto.tsv"}
OUTPUT_FILE = "stats_2.xlsx"

def dict_to_table_files_rows(data: dict, out_path: str):
    df = pd.DataFrame.from_dict(data, orient="index").fillna(0).astype(int)
    df.index.name = "file"
    df = df.reset_index()

    suffix = out_path.lower().rsplit(".", 1)[-1]
    if suffix == "xlsx":
        df.to_excel(out_path, index=False)
    elif suffix == "csv":
        df.to_csv(out_path, index=False)
    elif suffix == "tsv":
        df.to_csv(out_path, sep="\t", index=False)
    else:
        raise ValueError("Use .tsv, .csv, or .xlsx")

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

    count = {}

    # Load data
    folders = find_folders_with_files(DATA_FOLDER)
    folder_dict = {}
    for folder in folders:
        count[folder.name] = {}
        folder_dict[folder] = {}
        for annotator in REQUIRED_FILES:
            folder_dict[folder][annotator] = []
            tsv_file = folder / annotator
            doc = webanno_tsv_read_file(tsv_file)

            for annotation in doc.annotations:
                if annotation.layer not in count[folder.name]:
                    count[folder.name][annotation.layer] = 0
                count[folder.name][annotation.layer] += 1
                new_annotation = {"label": annotation.layer, "tokens": []}
                for token in annotation.tokens:
                    new_annotation['tokens'].append(f"{token.text}")
                # print(folder.name, annotator, new_annotation)
                print(folder.name, new_annotation['label'], " ".join(new_annotation['tokens']))
                folder_dict[folder][annotator].append(new_annotation)

    print(count)
    dict_to_table_files_rows(count, OUTPUT_FILE)
