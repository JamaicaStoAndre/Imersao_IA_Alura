# chatbot_pandas.py

import pandas as pd
from langchain.agents import create_pandas_dataframe_agent, AgentType
from langchain.chat_models import ChatOpenAI

# Substitua isso pela sua chave de API da OpenAI
openai_api_key = 'OPENAI_API_KEY'

def load_data(file_path):
    """Carrega dados do arquivo CSV em um DataFrame do pandas."""
    try:
        df = pd.read_csv(file_path)
        return df
    except Exception as e:
        raise ValueError(f"Erro ao carregar o arquivo: {str(e)}")

def analyze_document(file_path):
    """Analisa o documento carregado, retornando alguma métrica ou análise."""
    df = load_data(file_path)
    
    # Exemplo de análise: contar linhas e colunas
    analysis_result = f"O documento contém {df.shape[0]} linhas e {df.shape[1]} colunas."
    return analysis_result

def interact_with_document(file_path, question):
    """
    Usa o LangChain e a API da OpenAI para interagir com um documento, respondendo a perguntas.
    
    Args:
        file_path (str): O caminho para o arquivo a ser analisado.
        question (str): A pergunta feita pelo usuário.

    Returns:
        str: A resposta gerada pela API da OpenAI.
    """
    df = load_data(file_path)
    
    # Configuração do agente LangChain
    llm = ChatOpenAI(
        temperature=0, model="gpt-3.5-turbo-0613", openai_api_key=openai_api_key, streaming=True
    )

    pandas_df_agent = create_pandas_dataframe_agent(
        llm,
        df,
        verbose=True,
        agent_type=AgentType.OPENAI_FUNCTIONS,
        handle_parsing_errors=True,
    )
    
    # Executar o agente para processar a pergunta
    try:
        response = pandas_df_agent.run([question])
        return response
    except Exception as e:
        return f"Erro ao processar a pergunta: {str(e)}"
