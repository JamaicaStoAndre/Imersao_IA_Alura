import folium
from folium import plugins
from folium.plugins import BeautifyIcon



# Função para adicionar marcadores ao mapa
def adicionar_marcadores(mapa):
    # Exemplo de adicionar um marcador personalizado com BeautifyIcon
    icon = BeautifyIcon(
        number=3,
        icon_shape="marker",
        border_color='purple',
        text_color="#007799",
        background_color='yellow',
        inner_icon_style='font-size:12px;padding-top:-5px;', # Estilo do ícone interno
    )
    
    # Adiciona o marcador personalizado ao mapa
    folium.Marker(
        [-28.4790, -49.0426],
        popup='Estação 1 - Nível do Rio: 2.5m',
        icon=icon
    ).add_to(mapa)
    
   