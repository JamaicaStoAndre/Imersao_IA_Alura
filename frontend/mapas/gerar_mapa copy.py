import folium

#Mapa hidrológico
def criar_mapa_hidrologico():
    # Cria um mapa centrado em uma localização específica
    mapa = folium.Map(location=[-28.4800, -49.0069], zoom_start=13)
    
    # Aqui, você pode adicionar marcadores ou camadas adicionais ao mapa
    # Exemplo de adicionar um marcador:
    folium.Marker([-28.4800, -49.0069], popup='Hidrometeorologia').add_to(mapa)
    
    # Salva o mapa em um arquivo HTML
    mapa.save('static/mapa_hidrometeorologia.html')
    
    return mapa

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