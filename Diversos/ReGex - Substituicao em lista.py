import re

def encontrarnome(regex, ltxt):
    # Encontro o nome que quero
    for i in range(len(ltxt)):
        if regex.match(ltxt[i]):
            for j in range(i, len(ltxt) - 1):
                ltxt[j] = ltxt[j + 1]
                ltxt[j] = re.sub(r'[0-9]{1,3}', f'{j + 1}', ltxt[j])
    # Decremento 1 da lista
    ltxt.pop(len(ltxt) - 1)
    ltxt = "\n".join(ltxt)
    return ltxt

def programa1():
    # Declaro o txt string, lista e regex
    txt = """1- Patrícia
    2- Larissa
    3- Parla
    4- Márcio
    5- Natanael
    6- Natalina
    7- Jhenifer
    8- neemias
    9- Mateus
    10- Guilherme
    11- Esther
    12- Diego
    13- Angela
    14- Paulo
    15-Francisco
    16-nataniel
    17- Natália
    18- Luiz Guilherme
    19- Francys
    20- Ezequiel
    21-Beth
    22-Alessandro
    23-Millena
    24-Joyce
    25-Lorrayne
    26-Jânio
    27-Isaías
    28- Carol
    29- Maria Eduarda
    30-adriana
    31-janice
    32-Luiz lindo
    33- Breno iludido"""
    ltxt = txt.split("\n")
    regex = re.compile(r"[0-9]{1,2}-[\s]*Guilherme")
    # Tiro espaços em branco da lista
    for i in range(len(ltxt)):
        ltxt[i] = ltxt[i].strip()
    txt = encontrarnome(regex, ltxt)
    print(f'{txt}')


def programa2():
    arq = open('txt/ReGex - Substituição em lista/Lista in.txt', 'r', encoding='utf8')
    txt = arq.read()
    ltxt = txt.split('\n')
    nome = input('Nome a ser retirado\n')
    stringregex = r'[0-9]{1,3}-[\s]*'+ nome
    regex = re.compile(stringregex)
    txt = encontrarnome(regex, ltxt)
    arq = open('txt/ReGex - Substituição em lista/Lista out.txt', 'w', encoding='utf8')
    arq.write(txt)

programa1()
