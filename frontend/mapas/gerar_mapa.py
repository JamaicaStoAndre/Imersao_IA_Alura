import folium
from frontend.estacoes.estacoes_rio_tubarao import adicionar_marcadores
from frontend.mapas.legendas_rio_tubarao import adicionar_legenda

#Mapa hidrológico
def criar_mapa_hidrologico():
    # Cria um mapa centrado em uma localização específica
    mapa_tubarao = folium.Map(
        location=[-28.4800, -49.0069],
        zoom_start=13,
        tiles='OpenStreetMap'
    )
    
    # Adiciona os marcadores ao mapa
    adicionar_marcadores(mapa_tubarao)

    # Adiciona a legenda ao mapa
    adicionar_legenda(mapa_tubarao)
    
    # Salva o mapa em um arquivo HTML
    mapa_tubarao.save('static/mapa_hidrometeorologia.html')
    
    return mapa_tubarao

# Chamada da função mapa hidrológico
if __name__ == "__main__":
    criar_mapa_hidrologico()

#Mapa AQI
def criar_mapa_AQI():
    # Cria um mapa centrado em uma localização específica
    mapa = folium.Map(location=[-28.4800, -49.0069], zoom_start=13)
    
    # Aqui, você pode adicionar marcadores ou camadas adicionais ao mapa
    # Exemplo de adicionar um marcador:
    folium.Marker([-28.4800, -49.0069], popup='Qualidade do ar').add_to(mapa)
    
    # Salva o mapa em um arquivo HTML
    mapa.save('static/mapa_AQI.html')
    
    return mapa

# Chamada da função mapa hidrológico
if __name__ == "__main__":
    criar_mapa_AQI()