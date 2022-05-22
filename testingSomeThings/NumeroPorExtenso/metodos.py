#Aequivo para criar metodos uteis para funcionamento do programa ( class modulo)
class metodos:

#metodo para descobrir se é inteiro
    def isInt(value):
        try:
            int(value)
            return True
        except:
            return False