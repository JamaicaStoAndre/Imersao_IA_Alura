// Eventos de Minimização e Restauração do Chatbot
$(document).ready(function() {
    // Carregar o histórico da conversa
    loadConversationHistory();
    let conversation = JSON.parse(localStorage.getItem('chat_conversation')) || [];
    console.log('Histórico carregado:', conversation);
    // ---1-Inicia com o chatbot minimizado
    $('.chat_window').hide();
    $('#chatbot-minimized-icon').show();

    // 2---Função para minimizar a janela do chatbot
    window.minimizarPagina = function() {
        $('.chat_window').hide(); // Esconde a janela do chatbot
        $('#chatbot-minimized-icon').show(); // Mostra o ícone do chatbot minimizado
    };

    // 3---Evento de clique no ícone do chatbot minimizado para restaurar a janela do chatbot
    $('#chatbot-minimized-icon').click(function() {
        $(this).hide(); // Esconde o ícone minimizado
        $('.chat_window').show(); // Mostra a janela do chatbot
        $('#msg_input').focus(); // Define o foco no campo de entrada
    });
});
