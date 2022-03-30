while True:
    valor =int(input("Digite um valor: "))
    j=1
    resposta = ""
    for i in range (valor-1):
        if(j <= valor):
            print("\n Valor: ",valor,"\n J = ",j)
            resposta = "Triangulo"
            valor -= j
            j+=1
            print("\n Valor: ",valor,"\n J = ",j)
            
             

        else:
            break
            resposta = "nao e triangulo"
            
    print(resposta)
