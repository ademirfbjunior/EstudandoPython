class metodos:
    def __init__(self):
        pass
    def trianguloBurca (valor):
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
            return resposta


