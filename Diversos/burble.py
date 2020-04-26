def main():
    # atribui valor as variaveis n1 e n2
    n1 = float(input('primeiro número '))
    n2 = float(input('segundo número '))

    # se n2 for menor que n1 troca
    if n2 < n1:
        temp = n1
        n1 = n2
        n2 = temp

    # imprime n1 e n2 na tela
    print(n1, 'e', n2)


# chama a funcao main()
main()
