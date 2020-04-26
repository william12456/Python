def main():
    print('Consegui')
    print('Executou o main')


def name():
    name = input('Digite seu nome\n')
    print(name)
    print('Executou o name')


def funcparam(i, j):
    for a in range(i):
        print(j)
        print('executou fucparam')


print('Estou aqui')
main()
name()
funcparam(10, 'Yau seja louvado')
