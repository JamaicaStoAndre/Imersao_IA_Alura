/**
 * Returns the current datetime for the message creation.
 */
function getCurrentTimestamp() {
	return new Date();
}

/**
 * Renders a message on the chat screen based on the given arguments.
 * This is called from the `showUserMessage` and `showBotMessage`.
 */
function renderMessageToScreen(args) {
	// local variables
	let displayDate = (args.time || getCurrentTimestamp()).toLocaleString('pt-BR', {
		day: '2-digit',
        month: '2-digit',
        year: '2-digit',
        hour: '2-digit',
        minute: '2-digit'
	});
	let messagesContainer = $('.messages');

	// init element
	let message = $(`
	<li class="message ${args.message_side}">
		<div class="avatar"></div>
		<div class="text_wrapper">
			<div class="text">${args.text}</div>
			<div class="timestamp">${displayDate}</div>
		</div>
	</li>
	`);

	// add to parent
	messagesContainer.append(message);

	// animations
	setTimeout(function () {
		message.addClass('appeared');
	}, 0);
	messagesContainer.animate({ scrollTop: messagesContainer.prop('scrollHeight') }, 300);
}

/* Sends a message when the 'Enter' key is pressed.
 */
$(document).ready(function() {
    $('#msg_input').keydown(function(e) {
        // Check for 'Enter' key
        if (e.key === 'Enter') {
            // Prevent default behaviour of enter key
            e.preventDefault();
			// Trigger send button click event
            $('#send_button').click();
        }
    });
});

/**
 * Displays the user message on the chat screen. This is the right side message.
 */
function showUserMessage(message, datetime) {
	renderMessageToScreen({
		text: message,
		time: datetime,
		message_side: 'right',
	});
}

/**
 * Displays the chatbot message on the chat screen. This is the left side message.
 */
function showBotMessage(message, datetime) {
	renderMessageToScreen({
		text: message,
		time: datetime,
		message_side: 'left',
	});
}

// Função para enviar a mensagem para o backend 
function sendMessageToBackend(message) {
	if (!acceptUserInput) return; // Não enviar nova mensagem se a flag for false
    // Aqui, substitua o código AJAX conforme necessário para sua implementação
    $.ajax({
        url: '/chat',
        type: 'POST',
        contentType: 'application/json',
        data: JSON.stringify({ 'message': message }),
        success: function(data) {
            showBotMessage(data.response, new Date()); // Exibir resposta do bot
            addToConversation(data.response, 'bot'); // Adicionar resposta do bot à conversa
        },
        error: function(error) {
            console.error("Erro ao enviar mensagem para o backend:", error);
        }
    });
}

/**
 * Obtenha a entrada do usuário e mostre-a na tela ao clicar no botão.
 */
$('#send_button').on('click', function (e) {
    let userMessage = $('#msg_input').val().trim();
    if (userMessage !== '') {
        showUserMessage(userMessage, new Date()); // Mostrar mensagem do usuário
        addToConversation(userMessage, 'user'); // Adicionar à conversa
        $('#msg_input').val(''); // Limpar campo de entrada
        
        // Substituir randomstring() pela lógica de enviar para backend
        sendMessageToBackend(userMessage); // Função modificada para enviar para o backend
    }
});

// Variável para controlar se o chatbot deve responder a novas mensagens
let acceptUserInput = false;

// Função para adicionar mensagem ao histórico no localStorage
function addToConversation(message, sender) {
	console.log('Adicionando ao histórico 1:', { sender, message });
    // Recuperar a conversa atual do localStorage ou iniciar uma nova
    let conversation = JSON.parse(localStorage.getItem('chat_conversation')) || [];
    conversation.push({ sender, message, timestamp: new Date().toISOString() });
    localStorage.setItem('chat_conversation', JSON.stringify(conversation));
}

// Função para carregar e exibir o histórico da conversa
function loadConversationHistory() {
    let conversation = JSON.parse(localStorage.getItem('chat_conversation')) || [];
    conversation.forEach(entry => {
        if (entry.sender === 'user') {
            showUserMessage(entry.message, new Date(entry.timestamp));
        } else if (entry.sender === 'bot') {
            showBotMessage(entry.message, new Date(entry.timestamp));
        }
    });

    if (conversation.length === 0 && !acceptUserInput) {
        // Esta é a primeira carga e não há mensagens no histórico
        acceptUserInput = true;
        showBotMessage('Meu nome é Rob, como posso te chamar?');
    }
}

// Carregar o histórico da conversa e verificar a necessidade da mensagem de saudação quando a página é carregada
$(document).ready(function() {
    loadConversationHistory();
});
