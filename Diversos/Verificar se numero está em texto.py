num=1
texto="Eu sou o número 1"

#Verificar int numa string
#como num é um int entao precisa fazer conversao para str
if str(num) in texto:
    print(texto)

#verifica int não está na string
if not str(num) in texto:
    print(num)
