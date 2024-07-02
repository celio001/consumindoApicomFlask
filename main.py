import urllib.request, json
import os
from dotenv import load_dotenv

load_dotenv()

chave_api = os.environ['CHAVE_API']

resposta = urllib.request.urlopen(chave_api)

dados = resposta.read()

jsondata = json.loads(dados)

print(jsondata['results'])