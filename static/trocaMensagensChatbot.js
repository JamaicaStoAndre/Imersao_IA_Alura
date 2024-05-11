$(document).ready(function() {
    // Função para mostrar mensagens do usuário
    function showUserMessage(message, timestamp) {
        renderMessageToScreen({
            text: message,
            time: timestamp,
            message_side: 'right',
            avatar: '/static/img/guy.jpg', // caminho para a imagem do avatar do usuário
            background_color: 'blue' // cor de fundo para a mensagem do usuário
        });
    }

    // Função para mostrar mensagens do chatbot
    function showBotMessage(message, timestamp) {
        renderMessageToScreen({
            text: message,
            time: timestamp,
            message_side: 'left',
            avatar: '/static/img/guy.jpg', // caminho para a imagem do avatar do bot
            background_color: 'yellow' // cor de fundo para a mensagem do bot
        });
    }

    // Renderiza uma mensagem na tela do chat
    function renderMessageToScreen(args) {
        let displayDate = args.time.toLocaleString('pt-BR', {
            hour: '2-digit',
            minute: '2-digit',
        });
        let messagesContainer = $('.messages');
        let message = $(`
            <li class="message ${args.message_side} appeared" style="background-color: ${args.background_color};">
                <div class="avatar"><img src="${args.avatar}" alt="Avatar"></div>
                <div class="text_wrapper">
                    <div class="text">${args.text}</div>
                    <div class="timestamp">${displayDate}</div>
                </div>
            </li>
        `);
        messagesContainer.append(message);
        messagesContainer.animate({ scrollTop: messagesContainer.prop('scrollHeight') }, 300);
    }

    // Evento de clique no botão de enviar mensagem
    $('#send_button').click(function() {
        let userMessage = $('#msg_input').val().trim();
        if (userMessage !== '') {
            sendMessageToBackend(userMessage);
            $('#msg_input').val(''); // Limpa o campo de entrada após o envio
        }
    });

    // Função para enviar a mensagem para o backend
    function sendMessageToBackend(message) {
        $.ajax({
            url: '/chat',  // URL para a rota do Flask
            type: 'POST',
            contentType: 'application/json',
            data: JSON.stringify({ 'message': message }),
            success: function(data) {
                // Exibe a resposta do ChatGPT na interface do chatbot
                showBotMessage(data.response, new Date());
            },
            error: function(error) {
                console.error("Erro ao enviar mensagem para o backend:", error);
            }
        });
    }

    // Evento para tecla 'Enter' pressionada no input de mensagem
    $('#msg_input').keydown(function(e) {
        if (e.key === 'Enter') {
            e.preventDefault();
            $('#send_button').click();
        }
    });
});
