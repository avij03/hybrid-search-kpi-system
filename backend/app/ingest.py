import os
import json
import argparse
from datetime import datetime


def read_documents(input_dir):
    docs = []
    doc_id = 0

    for filename in os.listdir(input_dir):
        if filename.endswith(".txt"):
            filepath = os.path.join(input_dir, filename)

            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()

            paragraphs = [p.strip() for p in content.split("\n") if p.strip()]

            for para in paragraphs:
                doc = {
                    "doc_id": doc_id,
                    "title": f"Document {doc_id}",
                    "text": para,
                    "source": filename,
                    "created_at": datetime.utcnow().isoformat()
                }

                docs.append(doc)
                doc_id += 1

    return docs


def save_jsonl(docs, output_path):
    with open(output_path, "w", encoding="utf-8") as f:
        for doc in docs:
            f.write(json.dumps(doc) + "\n")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--out", required=True)

    args = parser.parse_args()

    docs = read_documents(args.input)

    os.makedirs(args.out, exist_ok=True)
    output_file = os.path.join(args.out, "docs.jsonl")

    save_jsonl(docs, output_file)

    print(f"Processed {len(docs)} documents")
    print(f"Saved to {output_file}")


if __name__ == "__main__":
    main()