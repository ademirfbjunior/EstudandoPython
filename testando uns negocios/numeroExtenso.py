
primeirosNumeros = ["zero","um","dois","tres","quatro","cinco","seis","sete","oito","nove","dez","onze","dose","treze","quatorze","quinze","dezeseis","dezesete","dezoito","dezenove"]

resposta = ""
# valor=int(input("Digite um valor: "))
for valor in range(100):
    unidade = valor // 1 % 10
    if valor < 20:
        resposta = primeirosNumeros[valor]
    #vinte
    elif valor < 30:
        if valor == 20:
            resposta = "vinte"
        else:
            resposta = "vinte e " + primeirosNumeros[unidade]
    #Trinta            
    elif valor < 40:
        if valor == 30:
            resposta = "trinta"
        else:
            resposta = "trinta e " + primeirosNumeros[unidade]
    #Quarenta
    elif valor < 50:
        if valor == 40:
            resposta = "quarenta"
        else:
            resposta = "quarenta e " + primeirosNumeros[unidade]
    #Cinquenta    
    elif valor < 60:
        if valor == 50:
            resposta = "cinquenta"
        else:
            resposta = "cinquenta e " + primeirosNumeros[unidade]
    #Sessenta
    elif valor < 70:
        if valor == 60:
            resposta = "sessenta"
        else:
            resposta = "sessenta e " + primeirosNumeros[unidade]
    #Setenta
    elif valor < 80:
        if valor == 70:
            resposta = "setenta"
        else:
            resposta = "setenta e " + primeirosNumeros[unidade]
    #oitenta
    elif valor < 90:
        if valor == 80:
            resposta = "oitenta"
        else:
            resposta = "oitenta e " + primeirosNumeros[unidade]
    #noventa   
    elif valor < 100:
        if valor == 90:
            resposta = "noventa"
        else:
            resposta = "noventa e " + primeirosNumeros[unidade]

    print(resposta)
