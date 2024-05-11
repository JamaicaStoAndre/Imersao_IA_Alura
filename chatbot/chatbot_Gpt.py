# chatbot/chatbot_Gpt.py
from openai import OpenAI

client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
import os

# Configura a chave da API da OpenAI e o CUSTOM_MODEL_ID a partir das variáveis de ambiente
CUSTOM_MODEL_ID = os.getenv('CUSTOM_MODEL_ID')

def get_chat_response(user_message, conversation_context=""):
    """
    Envia uma mensagem de usuário para a API da OpenAI e retorna a resposta do GPT.
    
    Parâmetros:
    - user_message (str): A mensagem do usuário para enviar ao GPT.
    - conversation_context (str): O contexto fixo que o GPT deve considerar na conversa.
    
    Retorna:
    - str: A resposta do GPT à mensagem do usuário.
    """
    response = client.completions.create(model=CUSTOM_MODEL_ID,  # Utiliza o ID do modelo personalizado
    prompt=f"{conversation_context}\n{user_message}",
    max_tokens=150)

    chat_response = response.choices[0].text.strip()
    return chat_response
