# init_chatbot.py

import os
from dotenv import load_dotenv, find_dotenv
from langchain.vectorstores import Chroma
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.memory import ConversationBufferMemory
from langchain_community.vectorstores import Chroma
from langchain_community.vectorstores import Chroma

import datetime

import openai

# Carregamento das configurações do ambiente
_ = load_dotenv(find_dotenv())

# Determinação do modelo baseado na data
current_date = datetime.datetime.now().date()
if current_date < datetime.date(2023, 9, 2):
    llm_name = "gpt-3.5-turbo-0301"
else:
    llm_name = "gpt-3.5-turbo"

# Inicialização do vectordb
persist_directory = 'docs/chroma/'
embedding = OpenAIEmbeddings()
vectordb = Chroma(persist_directory=persist_directory, embedding_function=embedding)

# Inicialização da memória
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
