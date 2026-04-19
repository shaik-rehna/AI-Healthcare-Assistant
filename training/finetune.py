from datasets import Dataset
import json

from transformers import (
    AutoTokenizer,
    AutoModelForCausalLM,
    TrainingArguments,
    Trainer
)

from peft import (
    LoraConfig,
    get_peft_model
)



# Load data

with open("training/train.json") as f:
    data = json.load(f)

dataset = Dataset.from_list(data)


# Load Gemma

model_name = "google/gemma-2-2b-it"

tokenizer = AutoTokenizer.from_pretrained(
    model_name
)

model = AutoModelForCausalLM.from_pretrained(
    model_name
)


# LoRA config

lora_config = LoraConfig(
    r=8,
    lora_alpha=16,
    target_modules=["q_proj","v_proj"],
    lora_dropout=0.05
)

model = get_peft_model(
    model,
    lora_config
)


# Tokenize

def tokenize(example):

    text = (
        example["instruction"]
        + "\n"
        + example["output"]
    )

    tokens = tokenizer(
        text,
        truncation=True,
        padding="max_length",
        max_length=256
    )

    tokens["labels"] = tokens["input_ids"].copy()

    return tokens

dataset = dataset.map(
    tokenize
)



# Train

training_args = TrainingArguments(

    output_dir="gemma-medical-lora",

    per_device_train_batch_size=1,

    num_train_epochs=3
)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=dataset
)

trainer.train()


model.save_pretrained(
"gemma-medical-lora"
)

tokenizer.save_pretrained(
"gemma-medical-lora"
)