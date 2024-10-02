from transformers import GPT2LMHeadModel, GPT2Tokenizer

def generate_response_from_llm (input_query_augmented):
    model_name = "openai-community/gpt2"
    model = GPT2LMHeadModel.from_pretrained(model_name)
    tokenizer = GPT2Tokenizer.from_pretrained(model_name)

    inputs = tokenizer.encode(input_query_augmented, return_tensors='pt')
    outputs = model.generate(inputs, max_length=500, num_return_sequences=1)

    generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return generated_text
