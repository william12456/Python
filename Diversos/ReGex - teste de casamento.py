#Teste para casamento em ReGex
import re
rex = re.compile("[a-z]")
st = input("str")
if rex.match(st):
    print("Casa")
else:
    print("Não casa")
rex.