/**
 * Este arquivo contém todas as funções JavaScript necessárias para o funcionamento do frontend do chatbot.
 * Inclui o envio de mensagens para o backend, exibição de mensagens na interface do usuário, e gerenciamento do histórico de conversas.
 */

// Variável para controlar se o chatbot deve responder a novas mensagens
let acceptUserInput = true;  // Inicialmente definido como true para permitir a entrada do usuário

/**
 * Função para adicionar mensagens ao histórico armazenado no localStorage.
 * @param {string} message - A mensagem a ser adicionada.
 * @param {string} sender - O remetente da mensagem ('user' ou 'bot').
 */
function addToConversation(message, sender) {
    console.log('Adicionando ao histórico:', { sender, message });
    let conversation = JSON.parse(localStorage.getItem('chat_conversation')) || [];
    conversation.push({ sender, message, timestamp: new Date().toISOString() });
    localStorage.setItem('chat_conversation', JSON.stringify(conversation));
}

/**
 * Função para enviar a mensagem para o backend via AJAX.
 * @param {string} message - A mensagem do usuário a ser enviada para o servidor.
 */
function sendMessageToBackend(message) {
    if (!acceptUserInput) return;
    showLoadingIndicator();  // Mostrar o indicador de carregamento ao enviar uma mensagem
    $.ajax({
        url: '/chat',
        type: 'POST',
        contentType: 'application/json',
        data: JSON.stringify({ 'message': message }),
        success: function(data) {
            hideLoadingIndicator();
            showBotMessage(data.response, new Date());  // Exibir resposta do bot
            addToConversation(data.response, 'bot');  // Adicionar resposta do bot à conversa
        },
        error: function(error) {
            hideLoadingIndicator();
            console.error("Erro ao enviar mensagem para o backend:", error);
        }
    });
}

/**
 * Função para exibir uma mensagem de carregamento enquanto aguarda a resposta.
 */
function showLoadingIndicator() {
    $('#loading_indicator').show();  // Supõe a existência de um elemento com id 'loading_indicator'
}

/**
 * Função para ocultar o indicador de carregamento após receber a resposta.
 */
function hideLoadingIndicator() {
    $('#loading_indicator').hide();
}

/**
 * Função para exibir mensagens do chatbot na interface do usuário.
 * @param {string} message - A mensagem a ser exibida.
 * @param {Date} datetime - O momento em que a mensagem foi recebida.
 */
function showBotMessage(message, datetime) {
    renderMessageToScreen({
        text: message,
        time: datetime,
        message_side: 'left',  // Mensagens do bot aparecem no lado esquerdo
    });
}

/**
 * Função para exibir mensagens do usuário na interface do usuário.
 * @param {string} message - A mensagem a ser exibida.
 * @param {Date} datetime - O momento em que a mensagem foi enviada.
 */
function showUserMessage(message, datetime) {
    renderMessageToScreen({
        text: message,
        time: datetime,
        message_side: 'right',  // Mensagens do usuário aparecem no lado direito
    });
}

/**
 * Função para renderizar uma mensagem na tela do chat.
 * @param {object} args - Contém texto, tempo, e lado da mensagem.
 */
function renderMessageToScreen(args) {
    let displayDate = (args.time || new Date()).toLocaleString('pt-BR', {
        day: '2-digit',
        month: '2-digit',
        year: '2-digit',
        hour: '2-digit',
        minute: '2-digit'
    });
    let messagesContainer = $('.messages');
    let message = $(`
        <li class="message ${args.message_side}">
            <div class="avatar"></div>
            <div class="text_wrapper">
                <div class="text">${args.text}</div>
                <div class="timestamp">${displayDate}</div>
            </div>
        </li>
    `);
    messagesContainer.append(message);
    setTimeout(() => {
        message.addClass('appeared');
    }, 0);
    messagesContainer.animate({ scrollTop: messagesContainer.prop('scrollHeight') }, 300);
}

/**
 * Configura o evento para enviar mensagem quando o usuário pressiona 'Enter'.
 */
$(document).ready(function() {
    $('#msg_input').keydown(function(e) {
        if (e.key === 'Enter') {
            e.preventDefault();
            $('#send_button').click();
        }
    });

    $('#send_button').on('click', function() {
        let userMessage = $('#msg_input').val().trim();
        if (userMessage !== '') {
            showUserMessage(userMessage, new Date());
            addToConversation(userMessage, 'user');
            $('#msg_input').val('');
            sendMessageToBackend(userMessage);
        }
    });

    loadConversationHistory();
});

/**
 * Função para carregar e exibir o histórico da conversa ao carregar a página.
 */
function loadConversationHistory() {
    let conversation = JSON.parse(localStorage.getItem('chat_conversation')) || [];
    conversation.forEach(entry => {
        if (entry.sender === 'user') {
            showUserMessage(entry.message, new Date(entry.timestamp));
        } else if (entry.sender === 'bot') {
            showBotMessage(entry.message, new Date(entry.timestamp));
        }
    });
}
