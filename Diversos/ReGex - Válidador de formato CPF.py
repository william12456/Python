#Verifica Formato de CPF
import re
rex = re.compile("[0-9]{3}.?[0-9]{3}.?[0-9]{3}-[0-9]{2}")
cpf = input("CPF")
if rex.match(cpf):
    print("CPF válido")
else:
    print("CPF inválido")