from peft import LoraConfig, get_peft_model
from transformers import AutoModelForCausalLM, AutoTokenizer, TrainingArguments, Trainer
import torch
import datasets

# Load dataset (assume preprocessed Q&A pairs)
dataset = datasets.load_dataset('json', data_files='../../data/energy_qa.json')

# Load base model and tokenizer
model_name = 'meta-llama/Llama-3.1-8B'
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name, load_in_4bit=True, device_map='auto')

# LoRA config
lora_config = LoraConfig(
    r=16,
    lora_alpha=32,
    target_modules=["q_proj", "v_proj"],
    lora_dropout=0.05,
    bias="none",
    task_type="CAUSAL_LM"
)
model = get_peft_model(model, lora_config)

# Training args
training_args = TrainingArguments(
    per_device_train_batch_size=2,
    num_train_epochs=1,
    fp16=True,
    output_dir="./lora_output",
    logging_steps=10,
    save_steps=50,
    evaluation_strategy="steps",
    eval_steps=50,
)

# Trainer
def preprocess(example):
    return tokenizer(example['question'] + '\n' + example['answer'], truncation=True, padding='max_length', max_length=512)

tokenized = dataset.map(preprocess)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized['train'],
    eval_dataset=tokenized['validation'],
)

trainer.train()
model.save_pretrained('./lora_output')
