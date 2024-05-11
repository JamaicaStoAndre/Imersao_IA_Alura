from folium.plugins import BeautifyIcon

def estilo_marcador_rio_tubarao():
    # Exemplo de definição de estilo de marcador com BeautifyIcon
    icon = BeautifyIcon(
        number=8,
        icon_shape="marker",
        border_color='purple',
        text_color="#007799",
        background_color='yellow',
        inner_icon_style='font-size:12px;padding-top:-5px;', # Estilo do ícone interno
    )
    return icon
