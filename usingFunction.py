# Criar um programa que calcula IMC, com validação de erros.
def ValidaIMC_Masculino(imc):
    if imc < 20.7:
        return "Abaixo Do Peso"
    elif 20.8 <= imc <= 26.4:
        return "Peso Normal"
    elif 26.5 <= imc <= 27.8:
        return "Sobrepeso"
    elif 27.9 <= imc <= 31.1:
        return "Acima do peso ideal"
    else:
        return "Obesidade"


def ValidaIMC_Feminino(imc):
    if imc < 19.1:
        return "Abaixo Do Peso"
    elif 19.2 <= imc <= 25.8:
        return "Peso Normal"
    elif 25.9 <= imc <= 27.3:
        return "Sobrepeso"
    elif 27.4 <= imc <= 32.3:
        return "Acima do peso ideal"
    else:
        return "Obesidade"


def validaMasculino_ou_Feminino():
    sexo = ""
    while True:
        try:
            sexo = input("Digite o sexo (Masculino [M] ou Feminino [F]").upper()
            sexo = float(sexo)
            print("Por favor digite apenas caracteres NÃO numerios!\n")
        except:
            sexo = sexo[0]
            if sexo == "F" or sexo == "M":
                break

            else:
                print("Valor Sexo invalido!\nTente novamente !\n")
    return sexo


def IMC(sexo, weight, height):
    valorImc = weight / (height * height)
    if sexo == 'F':
        print("Sexo: Feminino\nSituação:", ValidaIMC_Feminino(valorImc))

    else:
        print("Sexo: Masculino\nSituação:", ValidaIMC_Feminino(valorImc))


print("======= Calculando seu ICM =======\n\n")
nome = input("Digite o seu nome: ")

while True:
    try:
        peso = float(input("Digite o seu peso: "))
        if peso > 0:
            break
        else:
            print("\nDigite valor valido acima de 0")
    except:
        print(
            "\nDigite apenas valores númericos e caso tenha decimal, utilizar '.' [ex: 79.7]!\nTente novamente!\n")

while True:
    try:
        altura = float(input("Digite o sua Altura: "))
        if altura < 0:
            print("\nDigite valor valido acima de 0")
        else:
            break
    except:
        print(
            "\nDigite apenas valores númericos e caso tenha decimal, utilizar '.' [ex: 1.68]!\nTente novamente!\n")

print(nome)
IMC(validaMasculino_ou_Feminino(), peso, altura)

#mudei