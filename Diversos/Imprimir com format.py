def main():
    # .split serve para ler na mesma linha
    valor = input('Digite os valores').split(' ')
    a = int(valor[0])
    b = int(valor[1])
    c = int(valor[2])
    print('os valores de a, b e c são repectivamente {}, {} e {}'.format(a, b, c))


main()
