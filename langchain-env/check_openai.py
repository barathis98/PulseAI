from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),  
)

chat_completion = client.chat.completions.create(
    model = "gpt-3.5-turbo",
    messages= [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What is human life expectancy in the United States?"},
    ]
)

print(chat_completion.choices[0].message.content)