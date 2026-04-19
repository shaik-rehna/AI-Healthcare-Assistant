from datasets import Dataset
import json

with open("training/train.json") as f:

    data = json.load(f)

dataset = Dataset.from_list(data)

print(dataset)

print(dataset[0])