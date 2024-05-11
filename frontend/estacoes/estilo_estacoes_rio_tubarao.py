from folium.plugins import BeautifyIcon

def estilo_marcador_rio_tubarao(nivel):
    # Se o nível for "N/A", definir o ícone para preto
    if nivel == "N/A":
        cor_icon = "#595959"  # Preto
        cor_texto = "#FFFFFF"  # Branco para o texto, para contraste
    else:
        # Chama a função que define a cor baseada no nível
        cor_icon = definir_cor_marcador(nivel)
        cor_texto = "#000000"

    # Definição do estilo de marcador com BeautifyIcon
    icon = BeautifyIcon(
        number=nivel,
        icon_shape="marker",
        border_color='black',
        text_color=cor_texto,
        background_color=cor_icon,
        inner_icon_style='font-size:10px;padding-top:-5px;'
    )
    return icon

def definir_cor_marcador(nivel):
    # Definindo cores com base no nível
    if nivel < 0:
        return "#5066e0"  # Azul para níveis abaixo de 0
    elif 0 <= nivel <= 1:
        return "#86d384"  # Verde para níveis entre 0 e 1
    elif 1 < nivel <= 1.5:
        return "#ead887"  # Amarelo claro para níveis entre >1 e <= 1.5
    elif 1.5 < nivel <= 1.8:
        return "#e56f6f"  # Vermelho para níveis entre >1.5 e <= 1.8
    else:
        return "#c184e8"  # Roxo para níveis acima de 1.8

