from openai import OpenAI
client = OpenAI()

def generate_response(query):
    response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a helpful assistant. From the information passed in query, answer the question"},
        {"role": "user", "content": query}
    ]
    )
    return response