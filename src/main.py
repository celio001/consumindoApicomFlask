import urllib.request, json

url = 'https://api.themoviedb.org/3/discover/movie?sort_by=popularuty.desc&api_key=afa1e943edeedb9c083093f3434836f4'

resposta = urllib.request.urlopen(url)

dados = resposta.read()

jsondata = json.loads(dados)

print(jsondata['results'])