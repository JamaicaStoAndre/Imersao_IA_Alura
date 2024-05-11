"""
At the command line, only need to run once to install the package via pip:

$ pip install google-generativeai
"""

from pathlib import Path
import hashlib
import google.generativeai as genai

genai.configure(api_key="YOUR_API_KEY")

# Set up the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 0,
  "max_output_tokens": 8192,
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
]

model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest",
                              generation_config=generation_config,
                              safety_settings=safety_settings)

def extract_pdf_pages(pathname: str) -> list[str]:
  parts = [f"--- START OF PDF ${pathname} ---"]
  # Add logic to read the PDF and return a list of pages here.
  pages = []
  for index, page in enumerate(pages):
    parts.append(f"--- PAGE {index} ---")
    parts.append(page)
  return parts

convo = model.start_chat(history=[
  {
    "role": "user",
    "parts": extract_pdf_pages("<path>/document0.pdf")
  },
  {
    "role": "user",
    "parts": ["Este arquivo contém dados históricos de enchentes no rio tubarão\n"]
  },
  {
    "role": "user",
    "parts": extract_pdf_pages("<path>/document1.pdf")
  },
  {
    "role": "user",
    "parts": ["aqui apresentamos um panorama geral das estações de monitoramento\n"]
  },
  {
    "role": "user",
    "parts": extract_pdf_pages("<path>/document2.pdf")
  },
  {
    "role": "user",
    "parts": ["Neste documento encontramos um relatório sobre a qualidade do ar no brasil\nAgora me responda quais os decretos municipais de enchentes temos"]
  },
  {
    "role": "model",
    "parts": ["Os decretos municipais sobre enchentes e alagamentos em Tubarão, conforme o documento \"EnchentesTubarao.pdf\", são:\n\n**Inundações:**\n\n* Decreto n° 267 de 24/03/1974: declara estado de calamidade pública em todo o território do Município, em virtude da Enchente que atingiu drasticamente a Cidade de Tubarão. Com 199 óbitos.\n* Decreto n°1.762/97 de 03/02/1997: determina situação de emergência – Inundação.\n* Decreto n° 2.004/00 de 04/02/2001: declara situação anormal (Enxurrada – Inundação Brusca).\n* Decreto n° 2.054 de 02/10/2001: declara situação anormal caracterizada como emergência por transbordamento.\n* Decreto n° 2.284/2004 de 14/09/2004: declara situação anormal caracterizada de emergência por Inundação.\n* Decreto n° 2.599 de 07/01/2009: declara situação anormal caracterizada por emergência por (Enxurrada) Inundação Brusca.\n* Decreto n° 2.689 de 12/05/2010: declara situação anormal caracterizada de emergência por (Enxurrada) Inundação Brusca.\n\n**Alagamentos:**\n\n* Decreto n°1587/94 de 13/05/1994: declara situação anormal caracterizada como emergência por Alagamento.\n* Decreto n°1691/95 de 28/12/1995: declara situação anormal caracterizada como emergência devido ao agravamento do Decreto n°1689/1995 por Alagamento.\n* Decreto n°1645/95 de 23/01/1995: declara situação anormal caracterizada como emergência por Alagamento.\n* Decreto n°1689/95 de 26/12/1995: declara situação anormal caracterizada como emergência por Alagamento.\n* Decreto n°2.255 de 07/05/2004: decreta situação anormal caracterizada como emergência por Alagamento.\n* Decreto 2.765 de 20/01/2011: decreta situação de emergência por Alagamentos.\n\n**Enxurradas:**\n\n* Decreto n°267 de 24/03/1974: declara estado de calamidade pública em todo o território do Município em virtude da enorme enchente que assolou a cidade de Tubarão, havendo igualmente e registrar movimentos de massa (deslizamentos) e enxurradas. \n\n**Deslizamentos:**\n\n* Decreto n°267 de 24/03/1974: declara estado de calamidade pública em todo o território do Município por deslizamentos.\n* Decreto n° 2.054 de 02/10/2001: declara situação anormal caracterizada como emergência por Deslizamento de encostas\n* Decreto n°2.255 de 07/05/2004: determina situação anormal caracterizada como emergência por Deslizamento."]
  },
])

convo.send_message("YOUR_USER_INPUT")
print(convo.last.text)