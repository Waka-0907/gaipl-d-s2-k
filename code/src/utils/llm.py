from transformers import AutoModelForCausalLM, AutoTokenizer
from config import HUGGING_FACE_MODEL, HUGGING_FACE_TOKEN

# Load LLM model
tokenizer = AutoTokenizer.from_pretrained(HUGGING_FACE_MODEL, use_auth_token=HUGGING_FACE_TOKEN)
model = AutoModelForCausalLM.from_pretrained(HUGGING_FACE_MODEL, use_auth_token=HUGGING_FACE_TOKEN)

def generate_recommendations(prompt):
    inputs = tokenizer(prompt, return_tensors="pt", padding=True, truncation=True, max_length=1024)
    outputs = model.generate(**inputs, max_length=512, num_return_sequences=1)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)
