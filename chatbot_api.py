from flask import Flask, redirect, render_template, request, jsonify, session, send_from_directory, url_for, flash
from flask_cors import CORS
import os
from werkzeug.utils import secure_filename

#Chatbots
# from chatbot.chatbot_Gpt import get_chat_response
# from chatbot.chatbot_contextoGPT import ChatbotContextoGPT

#Flask
app = Flask(__name__)
CORS(app)
## 1-6-----------Chatbot PDF
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['SECRET_KEY'] = 'uma_chave_secreta_muito_segura'
app.config['ALLOWED_EXTENSIONS'] = {'txt', 'pdf'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route('/chatartigos')
def chatartigos():
    # A função render_template agora aponta para 'chatartigos.html'
    return render_template('chatartigos.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'document' not in request.files:
        flash('No file part')
        return redirect(url_for('chatartigos'))
    file = request.files['document']
    if file.filename == '':
        flash('No selected file')
        return redirect(url_for('chatartigos'))
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        flash('Upload feito com sucesso!!')
    # Nova lógica para ler o conteúdo do arquivo
        with open(file_path, 'r') as f:
            file_content = f.read()
        return render_template('chatartigos.html', file_content=file_content)
    else:
        flash('Tipo de arquivo inválido')
    return redirect(url_for('chatartigos'))
#
if __name__ == '__main__':
    app.run(debug=True)
