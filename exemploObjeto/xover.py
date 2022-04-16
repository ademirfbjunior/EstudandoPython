#Arquivo utilizado para testar algumas coisas antes de colocar em um progama

def isInt(value):
  try:
    int(value)
    return True
  except:
    return False

valor = input("Digite um valor inteiro: ")
            
if isInt(valor) :
    valor = int(valor)
else:
    print("TOMA")