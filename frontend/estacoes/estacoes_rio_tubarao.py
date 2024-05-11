import folium
from frontend.estacoes.estilo_estacoes_rio_tubarao import estilo_marcador_rio_tubarao

# Função para adicionar marcadores ao mapa
def adicionar_marcadores(mapa):
    # Definindo informações para cada estação (coordenadas, popup, nível e tooltip)
    estacoes = [
        {"coordenadas": [-28.424304702991968, -49.12287749287351], "popup": "Nome: TB151B Op:CPRM", "nivel": -1, "tooltip": "PEDRAS GRANDES"},
        {"coordenadas": [-28.42019995874658, -49.10598621814771], "popup": "Nome: RIO DO POUSO Op:EPAGRI-SC", "nivel": 0, "tooltip": "RIO DO POUSO"},
        {"coordenadas": [-28.474860104202456, -49.043751603912526], "popup": "Nome: TOMADA DAG US JL FAZ CRUZEIRO Op:CGT ELETROSUL", "nivel": 'N/A', "tooltip": "SÃO JOÃO"},
        {"coordenadas": [-28.480767900082217, -49.0391406660733], "popup": "Nome: TB164B Op:CPRM", "nivel": 1.5, "tooltip": "FRENTE PEDREIRA"},
        {"coordenadas": [-28.470109501152784, -48.99333126615157], "popup": "Nome: TOMADA D'ÁGUA US. JORGE LACERDA Op:CGT ELETROSUL", "nivel": 'N/A', "tooltip": "PONTE E.B. MARGEM ESQ."},
        {"coordenadas": [-28.470058879746055, -48.99182872900419], "popup": "Nome: TUBARÃO Op:EPAGRI-SC", "nivel": 1.8, "tooltip": "PONTE E.B. MARGEM DIR."},
        {"coordenadas": [-28.46464147984432, -48.98425111118565], "popup": "Nome: TUBARÃO - ESCRIT. FISC. DE OBRAS Op:DNOS", "nivel": 'N/A', "tooltip": "ESCRIT. FISC. DE OBRAS"},
        {"coordenadas": [-28.46162246909622, -48.97660876030802], "popup": "Nome: TUBARÃO  Op:SDE-SC", "nivel": 2, "tooltip": "Ponte trilho Passagem"},
        {"coordenadas": [-28.457701093799717, -48.984132353829054], "popup": "Nome: TB150B  Op:CPRM", "nivel": 4, "tooltip": "Bairro Sto André"},
        # Adicione outras estações conforme necessário
    ]
    
    # Iterando sobre as estações e adicionando marcadores ao mapa
    for estacao in estacoes:
        icon = estilo_marcador_rio_tubarao(estacao["nivel"])  # Chama a função dos estilos dos marcadores
        folium.Marker(
            location=estacao["coordenadas"],
            popup=estacao["popup"],
            tooltip=estacao.get("tooltip", "Informação indisponível"),  # Usa .get para evitar KeyError
            icon=icon
        ).add_to(mapa)
