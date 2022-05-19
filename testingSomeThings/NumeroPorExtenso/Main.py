#arquivo principal onde a magica acontece
from numeroExtenso import NumeroExtenso
from metodos import *

#Criando loop para testar varias vezes
while True:
    #loop para tratar expect e recebendo o valor em input
    while True:

        try:
            valor = input("Digite um valor inteiro: ")

            if metodos.isInt(valor) and 0 <= int(valor) <= 999:
                valor = int(valor)
                break

            elif float.is_integer(float(valor)) and 0 <= float(valor) <= 999:
                valor = float(valor)
                valor = int(valor)
                break

            else:
                raise Exception()
        except:
            print("\nValor digitado não Aceito !\nDigite numeros inteiros de 0 à 999\n")



    n1 = NumeroExtenso()

    result = n1.numeroExtensoResult(valor)

    print(result)

# #testando todos os numeros
# for i in range(1000):
#     print(NumeroExtenso().numeroExtensoResult(i))
#testing if git's works in my new laptop

