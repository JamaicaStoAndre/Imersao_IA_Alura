from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import os
import google.generativeai as genai
import logging

# Configuração de logging para capturar informações úteis durante o desenvolvimento
logging.basicConfig(level=logging.DEBUG)


# Carrega a chave da API do ambiente e configura o cliente genai
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY_2')
if GOOGLE_API_KEY is None:
    raise EnvironmentError("API key not found. Please set the GOOGLE_API_KEY environment variable.")
genai.configure(api_key=GOOGLE_API_KEY)

# Importações de módulos locais para funcionalidades adicionais
from frontend.mapas.gerar_mapa import criar_mapa_hidrologico, criar_mapa_AQI

app = Flask(__name__)
CORS(app)  # Configuração simplificada de CORS para permitir acesso de qualquer origem

# Configurações do modelo de IA, incluindo segurança e configurações de geração
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 0,
    "max_output_tokens": 8192,
}

safety_settings = [
    {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
]

# Criação do modelo GenerativeModel usando Gemini Pro
model = genai.GenerativeModel('gemini-pro')


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hidrometeorologia')
def hidrometeorologia():
    criar_mapa_hidrologico()
    return render_template('hidrometeorologia.html')

@app.route('/qualidadedoar')
def qualidadedoar():
    criar_mapa_AQI()
    return render_template('qualidadedoar.html')

@app.route('/chat', methods=['POST'])
def chat():
    try:
        user_input = request.json.get('message')
        if user_input:
            # Chamada simples do método generate_content com a entrada do usuário
            response = model.generate_content(user_input)
            return jsonify({'response': response.text})  # Retorna a resposta gerada pelo modelo
        else:
            return jsonify({'error': 'Mensagem vazia recebida'}), 400
    except Exception as e:
        logging.error(f"Error processing chat message: {str(e)}")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
