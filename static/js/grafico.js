// Dados de exemplo (elevação do rio a cada hora)
var dados = {
    labels: ['1h', '2h', '3h', '4h', '5h', '6h', '7h', '8h', '9h', '10h'],
    datasets: [{
        label: 'Elevação do Rio',
        backgroundColor: 'rgba(54, 162, 235, 0.2)',
        borderColor: 'rgba(54, 162, 235, 1)',
        borderWidth: 1,
        data: [-1, 0, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5] // Valores hipotéticos
    }]
};

// Configurações do gráfico
var opcoes = {
    responsive: true,
    maintainAspectRatio: false,
    scales: {
        yAxes: [{
            scaleLabel: {
                display: true,
                labelString: 'Elevação (m)'
            }
        }],
        xAxes: [{
            scaleLabel: {
                display: true,
                labelString: 'Hora'
            }
        }]
    }
};

// Inicializar o gráfico
document.addEventListener('DOMContentLoaded', function() {
    var ctx = document.getElementById('graficoElevacaoRio').getContext('2d');
    var myChart = new Chart(ctx, {
        type: 'line',
        data: dados,
        options: opcoes
    });
});
