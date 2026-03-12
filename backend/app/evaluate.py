import json
import numpy as np

def recall_at_k(relevant, retrieved, k):
    retrieved_k = retrieved[:k]
    return len(set(relevant) & set(retrieved_k)) / len(relevant)

def ndcg_at_k(relevant, retrieved, k):
    dcg = 0
    for i, doc in enumerate(retrieved[:k]):
        if doc in relevant:
            dcg += 1 / np.log2(i + 2)

    idcg = sum(1 / np.log2(i + 2) for i in range(min(len(relevant), k)))

    return dcg / idcg if idcg > 0 else 0