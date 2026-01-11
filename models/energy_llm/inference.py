from transformers import AutoTokenizer, AutoModelForCausalLM
from peft import PeftModel
import torch

def load_lora_adapter(base_model_path, lora_adapter_path):
    model = AutoModelForCausalLM.from_pretrained(base_model_path, load_in_4bit=True, device_map='auto')
    model = PeftModel.from_pretrained(model, lora_adapter_path)
    tokenizer = AutoTokenizer.from_pretrained(base_model_path)
    return model, tokenizer

def generate_answer(model, tokenizer, prompt):
    inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
    with torch.no_grad():
        outputs = model.generate(**inputs, max_new_tokens=128)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

if __name__ == "__main__":
    model, tokenizer = load_lora_adapter('meta-llama/Llama-3.1-8B', './lora_output')
    prompt = "What are the main challenges in oil production forecasting?"
    print(generate_answer(model, tokenizer, prompt))
