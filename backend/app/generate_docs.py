import os
import random

topics = [
    "machine learning",
    "cybersecurity",
    "vector databases",
    "information retrieval",
    "artificial intelligence",
    "cloud computing",
    "network security",
    "deep learning",
    "data engineering",
    "search systems"
]

templates = [
    "Recent advances in {topic} are transforming modern software systems.",
    "{topic} plays a critical role in large scale data processing pipelines.",
    "Researchers continue exploring new techniques in {topic} for improved performance.",
    "{topic} enables scalable solutions across distributed architectures.",
    "Many organizations rely on {topic} for mission critical applications."
]

os.makedirs("data/raw", exist_ok=True)

docs = []

for i in range(300):
    topic = random.choice(topics)
    sentence = random.choice(templates).format(topic=topic)

    paragraph = f"Document {i}. {sentence} This article discusses key concepts in {topic}."

    docs.append(paragraph)

with open("data/raw/corpus.txt", "w") as f:
    for doc in docs:
        f.write(doc + "\n\n")

print("Generated 300 documents.")