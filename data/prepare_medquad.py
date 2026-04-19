from datasets import load_dataset
import json

# Load MedQuAD
dataset = load_dataset(
    "lavita/MedQuAD",
    split="train"
)

print(dataset)
print(dataset[0])

# Convert first 500 examples into instruction format
examples = []

for row in dataset.select(range(500)):


    question = row["question"]
    answer = row["answer"]

    examples.append({
        "instruction": question,
        "output": answer
    })

with open(
    "training/train.json",
    "w"
) as f:
    json.dump(
        examples,
        f,
        indent=2
    )

print(
    len(examples),
    "examples saved."
)