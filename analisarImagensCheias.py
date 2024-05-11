"""
At the command line, only need to run once to install the package via pip:

$ pip install google-generativeai
"""

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

convo = model.start_chat(history=[
  {
    "role": "user",
    "parts": ["a imagem ilustra uma inundação em cidade com nível do rio em 1 metro  acima do normal\n"]
  },
  {
    "role": "user",
    "parts": ["esta imagem ilustra o nível do rio acima de 2 metros acima do normal\n"]
  },
  {
    "role": "user",
    "parts": ["a imagem ilustra o rio 0,5 metro acima do nível normal\n"]
  },
  {
    "role": "user",
    "parts": ["esta imagem ilustra o nível do rio com 3 metros acima do nível normal normal\n"]
  },
  {
    "role": "user",
    "parts": ["Qual nível do rio ?"]
  },
  {
    "role": "model",
    "parts": ["O nível do rio parece estar **2 metros acima do normal**. A água atingiu o topo das janelas do primeiro andar das casas, indicando uma inundação significativa."]
  },
])

convo.send_message("YOUR_USER_INPUT")
print(convo.last.text)