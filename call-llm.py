import json
import os
from pathlib import Path
import time

from dotenv import load_dotenv
from openai import OpenAI
from webanno_tsv import Document, webanno_tsv_read_file

TRAIN_LIST = [
    'P2_O2.txt', 'P2_O1.txt', 'P4_W1.txt', 'P4_W2.txt', 'P8_W2.txt',
    'P4_O1.txt', 'P8_O2.txt', 'P10_W2.txt', 'P1_O2.txt', 'P3_W2.txt',
    'P1_O1.txt', 'P3_O1.txt', 'P1_W1.txt', 'P5_W2.txt', 'P5_W1.txt',
    'P7_O2.txt', 'P5_O2.txt', 'P7_W1.txt', 'P7_W2.txt', 'P9_O1.txt',
]
TEST_LIST = ['P2_W2.txt', 'P2_W1.txt', 'P6_O2.txt', 'P8_W1.txt', 'P6_O1.txt', 'P8_O1.txt', 'P6_W2.txt', 'P4_O2.txt', 'P6_W1.txt', 'P3_W1.txt', 'P10_W1.txt', 'P10_O2.txt', 'P1_W2.txt', 'P10_O1.txt', 'P3_O2.txt', 'P9_W2.txt', 'P7_O1.txt', 'P9_W1.txt', 'P9_O2.txt', 'P5_O1.txt']

DATA_FOLDER = "annotation"
GOLD_FILE = "beatricebozzetto.tsv"
PROMPT_FILE = "prompt.md"
PROMPT_ZERO = "prompt-zero.md"
GUIDELINES_FILE = "guidelines.md"
EXAMPLE_FILE = "single-example.md"
OUTPUT_FOLDER = "llm_outputs"

KIND = "few_shot"


def load_files(data_folder: str, train_list: list[str], gold_file: str) -> dict[str, Document]:
    base_path = Path(data_folder)
    gold_contents: dict[str, Document] = {}

    for folder_name in train_list:
        folder_path = base_path / folder_name
        gold_path = folder_path / gold_file

        if not folder_path.is_dir():
            raise FileNotFoundError(f"Training folder not found: {folder_path}")
        if not gold_path.is_file():
            raise FileNotFoundError(f"Gold file not found: {gold_path}")

        gold_contents[folder_name] = webanno_tsv_read_file(gold_path)

    return gold_contents


if __name__ == "__main__":
    load_dotenv()

    openai_url = (os.getenv("OPENAI_BASE_URL") or "").strip() or None
    openai_token = (os.getenv("OPENAI_API_KEY") or "").strip()
    openai_model = (os.getenv("OPENAI_MODEL") or "").strip()

    if not openai_token:
        raise ValueError("Set OPENAI_API_KEY before running the script.")
    if not openai_model:
        raise ValueError("Set OPENAI_MODEL before running the script.")
    # if openai_url and not openai_url.startswith(("http://", "https://")):
    #     raise ValueError(
    #         "OPENAI_BASE_URL must start with http:// or https://, "
    #         f"got: {openai_url!r}"
    #     )

    if openai_url:
        print(f"Using custom OpenAI base URL: {openai_url}")
        client = OpenAI(api_key=openai_token, base_url=openai_url)
    else:
        client = OpenAI(api_key=openai_token, base_url="https://api.openai.com/v1")
    output_dir = Path(OUTPUT_FOLDER)
    output_dir = output_dir / f"{openai_model.replace('/', '_')}" / KIND
    output_dir.mkdir(parents=True, exist_ok=True)

    # Load prompt and guidelines
    if KIND == "few_shot":
        with open(PROMPT_FILE, "r", encoding="utf-8") as f:
            prompt = f.read()
    elif KIND == "zero_shot":
        with open(PROMPT_ZERO, "r", encoding="utf-8") as f:
            prompt = f.read()

    with open(GUIDELINES_FILE, "r", encoding="utf-8") as f:
        guidelines = f.read()
    with open(EXAMPLE_FILE, "r", encoding="utf-8") as f:
        example = f.read()
    
    prompt = prompt.replace("{{GUIDELINES}}", guidelines)
    test_files = load_files(DATA_FOLDER, TEST_LIST, GOLD_FILE)

    if KIND == "few_shot":
        all_examples = []
        gold_files = load_files(DATA_FOLDER, TRAIN_LIST, GOLD_FILE)
        for folder_name, content in gold_files.items():
            this_example = example

            this_example = this_example.replace("{{TEXT}}", content.text)

            annotations = []
            for annotation in content.annotations:
                annotations.append({"text": annotation.text, "type": annotation.layer.replace("webanno.custom.", "")})
            
            json_string = json.dumps(annotations, indent=2, ensure_ascii=False)
            this_example = this_example.replace("{{ANNOTATIONS}}", json_string)
            all_examples.append(this_example)
        
        prompt = prompt.replace("{{EXAMPLES}}", "\n\n".join(all_examples))

    for folder_name, content in test_files.items():
        this_prompt = prompt.replace("{{TEXT}}", content.text)

        output_path = output_dir / folder_name
        prompt_path = output_dir / f"{folder_name}.prompt.md"
        prompt_path.write_text(this_prompt, encoding="utf-8")

        if output_path.is_file():
            print(f"Output already exists for {folder_name}, skipping.")
            continue
        print(f"Processing {folder_name}, saving output to {output_path}")
        response = client.chat.completions.create(
            model=openai_model,
            messages=[
                {"role": "user", "content": this_prompt}
            ]
        )
        output_path.write_text(response.choices[0].message.content, encoding="utf-8")
        time.sleep(1)
        # break
