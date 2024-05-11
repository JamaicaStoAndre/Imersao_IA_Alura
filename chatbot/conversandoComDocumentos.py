#https://www.udemy.com/course/langchain-python-portuguese/learn/lecture/39489382#overview
#Conversando com nossos documentos
#instalar chromadb e tiktoken
from langchain.llms import OpenAI
from langchain.document_loaders import TextLoader #carrega os documentos e divide em pedaços
from langchain.text_splitter import RecursiveCharacterTextSplitter #carrega os documentos e divide em pedaços
from langchain.embeddings.openai import OpenAIEmbeddings # Ajudam a medir relação entre strings de texto
from langchain.vectorstores import Chroma # Banco de dados de vetores que usaremos para pegar nosso documento, obter os embeddings, em seguida salvar em um bando de dados de vetores para recuperação, que será o Chroma, que é executado localmente
from langchain.chains import RetrievalQA # ajuda  a procurar documentos relevantes em nossa base de dados Chroma e então fazer a pergunta relevante para esses dados, resultando em uma resposta

#Carregar documento
loader = TextLoader('/home/maykon/Documentos/1-DevJupyter/1-IAnalisesClimaticas/chatbot/data/hidrometeorologia.txt')

#Carregando o documento em uma variável
documentos = loader.load() #array

#Exibir no terminal o documento
#print(documentos)

#Dividir o documento em pedaços, pois se for muito grande o modelo não carrega
#primeiro vamos colocar os texto perto um do outro
texto_dividido = RecursiveCharacterTextSplitter(chunk_size=500 , chunk_overlap=100) # chunk_size= tamanho do bloco. chunk_overlap = sobreposição de pedaços
textos = texto_dividido.split_documents(documentos)

print(len(f"O tamanho de blocos é: {texto_dividido}"))
#print(textos[0])
#print(textos[1])

#Vamos criar nossos embeddings. Criar relação entre as palavras
embeddings = OpenAIEmbeddings()
documentosArmazenados = Chroma.from_documents(textos, embeddings, collection_name="ResumoPAP-52")
#chroma é um banco de dados de embeddings

#Vamos usar o bando de dados de vetores que acabamos de criar
llm= OpenAI(temperature=0)
chain = RetrievalQA.from_chain_type(llm, retriever=documentosArmazenados.as_retriever(), verbose=True)

#Fazer uma pergunta para o modelo
print(chain.run("qual finalidade do projeto?"))