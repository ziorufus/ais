from pathlib import Path
from typing import List
from webanno_tsv import webanno_tsv_read_file, Document
import pandas as pd
import openpyxl
from sklearn.preprocessing import MultiLabelBinarizer
from skmultilearn.model_selection import IterativeStratification

DATA_FOLDER = "annotation"
REQUIRED_FILES = {"beatricebozzetto.tsv"}
OUTPUT_FILE = "stats.xlsx"

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

    total_list = []
    X = []

    # Load data
    folders = find_folders_with_files(DATA_FOLDER)
    for folder in folders:
        for annotator in REQUIRED_FILES:

            label_list = set()
            if "_O" in str(folder):
                label_list.add("ORAL")
            elif "_W" in str(folder):
                label_list.add("WRITTEN")
            else:
                print("ERROR")
                continue

            tsv_file = folder / annotator
            doc = webanno_tsv_read_file(tsv_file)

            for annotation in doc.annotations:
                label_list.add(annotation.layer)
            
            total_list.append(list(label_list))
            X.append(str(folder.name))

    mlb = MultiLabelBinarizer()
    y = mlb.fit_transform(total_list)

    train_idx = test_idx = None
    while True:
        stratifier = IterativeStratification(n_splits=2, order=2, sample_distribution_per_fold=[0.5, 0.5])
        train_idx, test_idx = next(stratifier.split(X, y))
        if len(train_idx) == len(test_idx):
            break

    test_count = {}
    train_count = {}

    for c in mlb.classes_:
        test_count[c] = 0
        train_count[c] = 0
    
    for file_id in train_idx:
        for c, value in zip(mlb.classes_, y[file_id]):
            train_count[c] += int(value)
    for file_id in test_idx:
        for c, value in zip(mlb.classes_, y[file_id]):
            test_count[c] += int(value)
    
    print("### TRAIN ###")
    print("Files: ", [X[i] for i in train_idx])
    for k in train_count:
        print(k, train_count[k])
    
    print("### TEST ###")
    print("Files: ", [X[i] for i in test_idx])
    for k in test_count:
        print(k, test_count[k])
