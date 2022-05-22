#importando class para chamada de API "pip install requests"
import requests

#utilizando o endereco da api em uma variavel
url = 'https://economia.awesomeapi.com.br/all/USD-BRL'

#realizando a chamada da api e armazendo em uma variavel
response = requests.get(url)

#validando se a api respondeu, status 200 é exito.
if(response.status_code == 200):
    valorDolar = (response.json()['USD']['low'])
    print("o valor do dolar é de: R$",valorDolar)
else:
    print("Erro na api")


