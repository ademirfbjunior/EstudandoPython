#Class modulo, voltada pra a execução de numeros por extenso
class NumeroExtenso:
    def __init__(self):
        pass

    def unidade_dezena(self, valor):
        # unidade
        primeirosNumeros = ["zero", "um", "dois", "tres", "quatro", "cinco", "seis", "sete", "oito", "nove",
                            "dez", "onze", "dose", "treze", "quatorze", "quinze", "dezeseis", "dezesete", "dezoito", "dezenove"]
        # resposta = ""
        # valor=int(input("Digite um valor: "))
        unidade = valor // 1 % 10
        if valor < 20:
            return primeirosNumeros[valor]
        # vinte
        elif valor < 30:
            if valor == 20:
                return "vinte"
            else:
                return "vinte e " + primeirosNumeros[unidade]
        # Trinta
        elif valor < 40:
            if valor == 30:
                return "trinta"
            else:
                return "trinta e " + primeirosNumeros[unidade]
        # Quarenta
        elif valor < 50:
            if valor == 40:
                return "quarenta"
            else:
                return "quarenta e " + primeirosNumeros[unidade]
        # Cinquenta
        elif valor < 60:
            if valor == 50:
                return "cinquenta"
            else:
                return "cinquenta e " + primeirosNumeros[unidade]
        # Sessenta
        elif valor < 70:
            if valor == 60:
                return "sessenta"
            else:
                return "sessenta e " + primeirosNumeros[unidade]
        # Setenta
        elif valor < 80:
            if valor == 70:
                return "setenta"
            else:
                return "setenta e " + primeirosNumeros[unidade]
        # oitenta
        elif valor < 90:
            if valor == 80:
                return "oitenta"
            else:
                return "oitenta e " + primeirosNumeros[unidade]
        # noventa
        elif valor < 100:
            if valor == 90:
                return "noventa"
            else:
                return "noventa e " + primeirosNumeros[unidade]

    # for i in range(100):
    #     print(unidade_dezena(i))

    def centena(self, valor):

        unidade = valor // 1 % 10
        dezena = (valor // 10 % 10) * 10
        dezena_unidade = dezena + unidade
        # 100
        if valor < 200:
            if valor == 100:
                return "cem"
            else:
                return "cento e " + self.unidade_dezena(dezena_unidade)
        # 200
        elif valor < 300:
            if valor == 200:
                return "duzentos"
            else:
                return "duzentos e " + self.unidade_dezena(dezena_unidade)
        # 300
        elif valor < 400:
            if valor == 300:
                return "trezentos"
            else:
                return "trezentos e " + self.unidade_dezena(dezena_unidade)
        # 400
        elif valor < 500:
            if valor == 400:
                return "quatrocentos"
            else:
                return "quatrocentos e " + self.unidade_dezena(dezena_unidade)
        # 500
        elif valor < 600:
            if valor == 500:
                return "quinhentos"
            else:
                return "quinhentos e " + self.unidade_dezena(dezena_unidade)
        # 600
        elif valor < 700:
            if valor == 600:
                return "Seissentos"
            else:
                return "Seissentos e " + self.unidade_dezena(dezena_unidade)
        # 700
        elif valor < 800:
            if valor == 700:
                return "setessentos"
            else:
                return "setessentos e " + self.unidade_dezena(dezena_unidade)
        # 800
        elif valor < 900:
            if valor == 800:
                return "oitossentos"
            else:
                return "oitossentos e " + self.unidade_dezena(dezena_unidade)
        # 900
        elif valor < 1000:
            if valor == 900:
                return "novessentos"
            else:
                return "novessentos e " + self.unidade_dezena(dezena_unidade)

        # valor = int(input("\nDigite um numero: "))

    def numeroExtensoResult(self, valor):
        if valor < 100:
            return(self.unidade_dezena(valor).title())
        elif valor < 1000:
            return(self.centena(valor).title())
