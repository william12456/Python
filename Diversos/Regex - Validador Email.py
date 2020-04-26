import re

regex = re.compile("[a-zA-Z0-9*.+_]+@gmail|hotmail|outlook\.com")
email = input("Digite seu Email\n")
if regex.match(email):
    print("É Válido")