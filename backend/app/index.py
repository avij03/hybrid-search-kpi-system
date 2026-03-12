import json
import argparse
import os
import pickle
from rank_bm25 import BM25Okapi


def load_documents(path):
    docs = []
    texts = []

    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            doc = json.loads(line)
            docs.append(doc)

            combined = (doc["title"] + " " + doc["text"]).lower()
            tokens = combined.split()
            texts.append(tokens)

    return docs, texts


def build_index(texts):
    bm25 = BM25Okapi(texts)
    return bm25


def save_index(index, docs, out_dir):
    os.makedirs(out_dir, exist_ok=True)

    path = os.path.join(out_dir, "bm25.pkl")

    with open(path, "wb") as f:
        pickle.dump({
            "index": index,
            "docs": docs
        }, f)

    print(f"BM25 index saved to {path}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--out", required=True)

    args = parser.parse_args()

    docs, texts = load_documents(args.input)
    index = build_index(texts)

    save_index(index, docs, args.out)


if __name__ == "__main__":
    main()