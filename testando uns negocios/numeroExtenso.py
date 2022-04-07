
def unidade_dezena (valor):
    #unidade
    primeirosNumeros = ["zero","um","dois","tres","quatro","cinco","seis","sete","oito","nove","dez","onze","dose","treze","quatorze","quinze","dezeseis","dezesete","dezoito","dezenove"]
    # resposta = ""
    # valor=int(input("Digite um valor: "))
    unidade = valor // 1 % 10
    if valor < 20:
        return  primeirosNumeros[valor]
    #vinte
    elif valor < 30:
        if valor == 20:
            return "vinte"
        else:
            return "vinte e " + primeirosNumeros[unidade]
    #Trinta            
    elif valor < 40:
        if valor == 30:
            return "trinta"
        else:
            return "trinta e " + primeirosNumeros[unidade]
    #Quarenta
    elif valor < 50:
        if valor == 40:
            return "quarenta"
        else:
            return "quarenta e " + primeirosNumeros[unidade]
    #Cinquenta    
    elif valor < 60:
        if valor == 50:
            return "cinquenta"
        else:
            return "cinquenta e " + primeirosNumeros[unidade]
    #Sessenta
    elif valor < 70:
        if valor == 60:
            return "sessenta"
        else:
            return "sessenta e " + primeirosNumeros[unidade]
    #Setenta
    elif valor < 80:
        if valor == 70:
            return "setenta"
        else:
            return "setenta e " + primeirosNumeros[unidade]
    #oitenta
    elif valor < 90:
        if valor == 80:
            return "oitenta"
        else:
            return "oitenta e " + primeirosNumeros[unidade]
    #noventa   
    elif valor < 100:
        if valor == 90:
            return "noventa"
        else:
            return "noventa e " + primeirosNumeros[unidade]

# for i in range(100):
#     print(unidade_dezena(i))

def centena(valor):
    
    if valor == 100:
        return "Cem"
    else:
        return "cento e " + unidade_dezena(valor)
    

while True:
    valor = int(input("\nDigite um numero: "))
    print(centena(valor))