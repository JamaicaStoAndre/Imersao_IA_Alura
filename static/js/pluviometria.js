document.addEventListener('DOMContentLoaded', function() {
    // Dados de exemplo (pluviometria em diferentes períodos)
    var dadosPluviometria = {
        labels: ['1h', '2h', '3h', '4h', '5h', '6h', '7h', '8h', '9h', '10h'],
        datasets: [{
            label: 'Pluviometria',
            backgroundColor: 'rgba(75, 192, 192, 0.2)',
            borderColor: 'rgba(75, 192, 192, 1)',
            borderWidth: 1,
            data: [20, 40, 60, 80, 100, 120, 140, 160, 180, 200] // Valores hipotéticos
        }]
    };

    // Configurações do gráfico
    var opcoesPluviometria = {
        responsive: true,
        maintainAspectRatio: false,
        scales: {
            yAxes: [{
                scaleLabel: {
                    display: true,
                    labelString: 'Precipitação (mm)'
                },
                ticks: {
                    beginAtZero: true,
                    max: 300 // Valor máximo de precipitação
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
    var ctxPluviometria = document.getElementById('graficoPluviometria').getContext('2d');
    var myChartPluviometria = new Chart(ctxPluviometria, {
        type: 'bar',
        data: dadosPluviometria,
        options: opcoesPluviometria
    });
});
