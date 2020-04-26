from threading import Thread
import threading


def NaturalNo():
    print(threading.current_thread().getName() + "  ", "   Has Started   ")
    for x in range(10):
        # Conversão de Int para str(string)
        # Para poder concatenar com o "  "
        print(str(x) + "  ")

    print(threading.current_thread().getName() + "  ", "   Has Ended   ")


def Arg1(nome):
    print(nome)




def Arg2(nome1,nome2):
    print(f'{nome1} é irmão de {nome2}')


# t1 e t2 excutao a mesma funcao paralelamente
t1 = Thread(target=NaturalNo)
t2 = Thread(target=NaturalNo)
# No t3 uso o args para passar um argumento
# No t4 uso o args para passar dois argumentos
t3 = Thread(target=Arg1, args=('Guilherme',))
t4 = Thread(target=Arg2, args=('Guilherme', 'Diana'))
# inicia as threads
t1.start()
t2.start()
t3.start()
t4.start()