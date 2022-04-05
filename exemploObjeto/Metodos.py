class metodos:
    def __init__(self):
        pass
    def ValidaTrianguloBolinhasDeGudi(valor):
        meuTexto = ""
        bolinhas = []
        bolinhas[1] = "*"
    
        resposta = ""
        if valor == 1:
            resposta = resposta = """ 
                -------------------------
                |  não é um  Triangulo  |
                ------------------------- 
                """
            meuTexto = bolinhas 
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
                    
                    meuTexto += (" "*i) + """\ """ + bolinhas*i+ "/\n"
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
            print(meuTexto)        
            return resposta 
 #testando um negocio
