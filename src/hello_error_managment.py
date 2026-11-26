from openai import OpenAI, AuthenticationError, RateLimitError, APIConnectionError
from dotenv import load_dotenv

load_dotenv()

def call_ai(question:str) -> str:
    client = OpenAI()

    try:
        response= client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "user",
                    "content": question
                }
            ],
            max_tokens=500,
            temperature=0.7
        )
        return response.choices[0].message.content

    except AuthenticationError:
        print("APIKEY inválida. Revisa tu archivo .env")
        raise SystemExit(1)
    
    except RateLimitError:
        print("Límite de velocidad alcanzado. Espera un momento.")
        raise SystemExit(1)
    
    except APIConnectionError:
        print("Sin conexión a la API. Revisa tu internet.")
    
    except Exception as e:
        print(f"Error inesperado: {type(e).__name__}: {e}")
        raise

if __name__ == "__main__":
    response = call_ai("Dame un título para un video de Python")
    print(f"AI: {response}")