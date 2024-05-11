# chatbot/chatbotDocs.py

from langchain.chains import ConversationalRetrievalChain
from langchain_community.vectorstores import Chroma


class ChatbotDocs:
    def __init__(self, llm, vectordb, memory):
        self.qa_chain = ConversationalRetrievalChain.from_llm(
            llm,
            retriever=vectordb.as_retriever(),
            memory=memory
        )

    def process_question(self, user_message):
        result = self.qa_chain({"question": user_message})
        chat_response = result['answer']  # Ajuste conforme a estrutura de 'result'
        return chat_response
