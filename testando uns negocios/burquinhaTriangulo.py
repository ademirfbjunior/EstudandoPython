while True:
    valor = int(input("Digite um valor: "))
    resposta = ""
    if valor == 1:
        resposta = resposta = """ 
            -------------------------
            |  não é um  Triangulo  |
            ------------------------- 
            """
    else:
        for i in range(valor):
            i += 1
            if (i) <= valor:
                resposta = """ 
                ---------------
                |  Triangulo  |
                ---------------
                """
                valor -= (i)
                i -= 1
                print("i=",i,"\nvalor=", valor)

            else:
                if valor == 0:
                    break
                else:
                    resposta = resposta = """ 
                -------------------------
                |  não é um  Triangulo  |
                ------------------------- 
                """
                    break
    print()
    print(resposta)
#