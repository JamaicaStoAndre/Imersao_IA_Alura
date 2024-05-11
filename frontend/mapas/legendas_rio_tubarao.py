# mapas/legendas_rio_tubarao.py

import folium

def adicionar_legenda(mapa_tubarao):
    # HTML para a legenda
    legend_html = """
    <div style="position: fixed;
         bottom: 10px;
         left: 10px;
         width: 200px;
         height: 150px;
         background-color: white;
         border:2px solid grey;
         z-index:9999;
         font-size:14px;">
         &nbsp;<b>Legenda:</b><br>
         &nbsp;<i class="fa fa-circle fa-1x" style="color:#5066e0"></i>&nbsp;Baixo<br>
         &nbsp;<i class="fa fa-circle fa-1x" style="color:#86d384"></i>&nbsp;Normal<br>
         &nbsp;<i class="fa fa-circle fa-1x" style="color:#ead887"></i>&nbsp;Atenção<br>
         &nbsp;<i class="fa fa-circle fa-1x" style="color:#e56f6f"></i>&nbsp;Alerta<br>
         &nbsp;<i class="fa fa-circle fa-1x" style="color:#c184e8"></i>&nbsp;Emergência<br>
         &nbsp;<i class="fa fa-circle fa-1x" style="color:#000000"></i>&nbsp;N/A-Inoperante<br>
    </div>
    """
    # Adiciona a legenda ao mapa
    mapa_tubarao.get_root().html.add_child(folium.Element(legend_html))
