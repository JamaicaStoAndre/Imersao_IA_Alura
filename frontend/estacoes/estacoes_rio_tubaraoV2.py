import folium
from folium import plugins
from estacoes.estilo_estacoes_rio_tubarao import estilo_marcador_rio_tubarao

# Função para adicionar marcadores ao mapa
def adicionar_marcadores(mapa):
    icon = estilo_marcador_rio_tubarao()  # Chama a função dos estilos dos marcadores
        
    # Adiciona o marcador personalizado ao mapa
    folium.Marker(
        [-28.4790, -49.0426],
        popup='Estação 1 - Nível do Rio: 2.5m',
        icon=icon
    ).add_to(mapa)    
   