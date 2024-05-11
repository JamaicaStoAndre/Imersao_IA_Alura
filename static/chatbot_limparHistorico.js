// Função para limpar o histórico de conversas do chatbot
function limparHistoricoChatbot() {
    // Verifica se existe um item 'chat_conversation' no localStorage
    if (localStorage.getItem('chat_conversation')) {
        // Remove o item 'chat_conversation' para limpar o histórico
        localStorage.removeItem('chat_conversation');
        console.log('Histórico do chatbot limpo com sucesso.');
    } else {
        console.log('Não há histórico de conversa do chatbot para limpar.');
    }
}

// Opção para executar a limpeza imediatamente ao carregar o script (remova se não desejar essa automação)
// limparHistoricoChatbot();
