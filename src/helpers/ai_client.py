"""Helper para crear y ejecutar el cliente"""
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI()

def call_ai(messages: list, temperature: float = 0.1) -> str:
    """Función que ejecuta el cliente"""
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
        temperature=temperature
    )

    return response.choices[0].message.content