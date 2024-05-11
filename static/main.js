$(document).ready(function() {
    // Iniciar com o chatbot minimizado
    $('.chat_window').hide();
    $('#chatbot-minimized-icon').show();

	// Evento de clique no ícone de minimizar
    $('#minimize_chat').click(function() {
        $('.chat_window').hide(); // Esconde a janela do chatbot
        $('#chatbot-minimized-icon').show(); // Mostra o ícone do chatbot minimizado
    });

    // Evento de clique no ícone de fechar
    $('#close_chat').click(function() {
        $('.chat_window').hide(); // Esconde a janela do chatbot
        // Aqui você pode decidir se quer esconder o ícone minimizado também ou se quer fechar completamente o chatbot
    });

    $('#chatbot-minimized-icon').click(function() {
        $(this).hide();
        $('.chat_window').show();
        // Exibir a mensagem de saudação apenas na primeira vez que o chatbot é aberto
        if ($('.messages .message').length === 0) {
            showBotMessage('Olá, posso ajudar?', new Date());
        }
        $('#msg_input').focus(); // Define o foco no campo de entrada
    });

    // Função para mostrar mensagens do usuário
    function showUserMessage(message, timestamp) {
        renderMessageToScreen({
            text: message,
            time: timestamp,
            message_side: 'right',
        });
    }

    // Função para mostrar mensagens do chatbot
    function showBotMessage(message, timestamp) {
        renderMessageToScreen({
            text: message,
            time: timestamp,
            message_side: 'left',
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
            <li class="message ${args.message_side} appeared">
                <div class="avatar"></div>
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
    $('#send_button').on('click', function () {
        let userMessage = $('#msg_input').val().trim();
        if (userMessage !== '') {
            sendMessageToBackend(userMessage);
        }
    });

    // Função para enviar a mensagem para o backend
    function sendMessageToBackend(message) {
        $.ajax({
            url: '/chatdoc',  // URL para a rota do Flask
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

    // Garantir que a mensagem de saudação seja exibida somente uma vez
    if ($('.messages .message').length === 0) {
        showBotMessage('Olá, posso ajudar?', new Date());
    }
});
