import json
import argparse
import os
import pickle
import numpy as np
import faiss
from sklearn.feature_extraction.text import TfidfVectorizer


def load_documents(path):
    docs = []
    texts = []

    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            doc = json.loads(line)
            docs.append(doc)
            texts.append(doc["title"] + " " + doc["text"])

    return docs, texts


def build_embeddings(texts):
    vectorizer = TfidfVectorizer()
    matrix = vectorizer.fit_transform(texts)
    embeddings = matrix.toarray().astype("float32")

    return vectorizer, embeddings


def build_faiss_index(embeddings):
    dim = embeddings.shape[1]
    index = faiss.IndexFlatL2(dim)
    index.add(embeddings)
    return index


def save_index(index, docs, vectorizer, out_dir):
    os.makedirs(out_dir, exist_ok=True)

    index_path = os.path.join(out_dir, "vector.index")
    meta_path = os.path.join(out_dir, "vector_meta.pkl")

    faiss.write_index(index, index_path)

    with open(meta_path, "wb") as f:
        pickle.dump({
            "docs": docs,
            "vectorizer": vectorizer
        }, f)

    print("Vector index saved.")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--out", required=True)

    args = parser.parse_args()

    docs, texts = load_documents(args.input)

    vectorizer, embeddings = build_embeddings(texts)

    index = build_faiss_index(embeddings)

    save_index(index, docs, vectorizer, args.out)


if __name__ == "__main__":
    main()