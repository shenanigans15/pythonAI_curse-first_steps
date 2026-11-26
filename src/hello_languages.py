from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {
            "role": "user",
            "content": "Di hola en 3 idiomas"
        }
    ]
)

text = response.choices[0].message.content
print(text)

print("\n--Uso de tokens--")
print(f"Tokens de entrada: {response.usage.prompt_tokens}")
print(f"Tokens de salida: {response.usage.completion_tokens}")
print(f"Tokens totales: {response.usage.total_tokens}")

cost_input = (response.usage.prompt_tokens / 1_000_000) * 0.15
cost_output = (response.usage.completion_tokens / 1_000_000) * 0.60
cost_total = cost_input + cost_output

print(f"\nCosto estimado: ${cost_total:.6f} USD")
print(f"\nID de la respuesta: {response.id}")
print(f"\nModelo utilizado: {response.model}")