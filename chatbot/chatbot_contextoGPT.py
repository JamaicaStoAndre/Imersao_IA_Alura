# chatbot/chatbot_contextoGPT.py

from openai import OpenAI
import os

api_key = os.getenv('OPENAI_API_KEY')
client = OpenAI(api_key=api_key)

# Configura a chave da API da OpenAI

class ChatbotContextoGPT:
    def __init__(self):
        self.messages = []
        self.context = "Você será um assistente meteorológico e hidrometeorológico. Você fará consultas em api e sites para informações sobre o tempo, chuvas, etc.Seu nome é Rob, você é um assistente virtual.Foi desenvolvido por João Maykon, morador da comunidade do bairro Santo André em Capivari de Baixo. Responda com textos curtos e diretos. NÃO saia do contexto de meteorologia e afins. Seja cordial, direto e simpático"

    def add_message(self, role, content):
        self.messages.append({"role": role, "content": content})

    def get_response(self, user_message):
        self.add_message("user", user_message)
        response = client.chat.completions.create(model="gpt-3.5-turbo-0125",
        messages=[{"role": "system", "content": self.context}] + self.messages,
        max_tokens=150,
        temperature=0.7,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0)
        chat_response = response.choices[0].message.content.strip()
        # Adiciona a resposta do bot ao histórico para manter o contexto
        self.add_message("assistant", chat_response)
        return chat_response
