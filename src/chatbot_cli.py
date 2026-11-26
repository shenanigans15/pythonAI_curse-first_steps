"""
Proyecto: CLI Chatbot
"""
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

# Configuracion
MODEL = "gpt-4o-mini"

SYSTEM_PROMPT = """Eres un asistente técnico experto en Python e IA.
Eres directo, usas ejemplos de código cuando es relevante,
y respondes en el mismo idioma que el usuario.
Si no sabes algo, lo dices honestamente."""

# Costos de la API en USD
COSTO_INPUT_POR_MILLON = 0.15
COSTO_OUTPUT_POR_MILLON = 0.60

class Chatbot:
    def __init__(self, system_prompt: str = SYSTEM_PROMPT):
        self.client = OpenAI()
        self.model = MODEL

        self.history: list[dict] = [
            {"role": "system", "content": system_prompt}
        ]

        self.total_tokens = 0
        self.total_cost = 0.0

    def chat(self, user_message: str) -> str:
        """Envía un mensaje y obtiene respesta manteniendo el historial"""

        self.history.append({
            "role": "user",
            "content": user_message
        })

        response = self.client.chat.completions.create(
            model=self.model,
            messages=self.history,
            max_tokens=1000,
            temperature=0.7
        )

        reponse = response.choices[0].message.content

        self.history.append({
            "role": "assistant",
            "content": response
        })

        return response

def main():
    """Función principal"""
    print("╔══════════════════════════════════════╗")
    print("║      Python IA Aplicada - Chatbot    ║")
    print("║  Escribe 'quit' o Ctrl+C para salir  ║")
    print("╚══════════════════════════════════════╝\n")


if __name__ == "__main__":
    main()
