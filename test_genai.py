from google import genai
from google.genai.types import HttpOptions
import os

# Verifica se as variáveis de ambiente necessárias estão definidas
project_id = os.environ.get("GOOGLE_CLOUD_PROJECT")
if not project_id:
    print("AVISO: GOOGLE_CLOUD_PROJECT não definido.")

print(f"Usando projeto: {project_id}")

try:
    # Inicializa o cliente GenAI
    client = genai.Client(http_options=HttpOptions(api_version="v1"))
    
    model_name = "gemini-3.5-flash"
    
    print(f"Enviando solicitação para o modelo: {model_name}...")
    response = client.models.generate_content(
        model=model_name,
        contents="Como o sistema de scripts está organizado no meu computador?",
    )
    print("\nResposta da IA:")
    print(response.text)

except Exception as e:
    print(f"\nErro ao chamar a API: {e}")
    print("\nVerifique se o modelo está habilitado no Model Garden do Vertex AI.")
