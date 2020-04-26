#definicao das classes
class teste:
    def metodo():
        print('z')

class testex:
    def metodox():
        print('x')

class testey:
    def metodoy():
        print('y')

#essa classe herda das classes testex e testey
class testexy(testex,testey):
    def metodoxy():
        print('xy')

#nessa linha eu chamo o metodo com o nome da classe
teste.metodo()
#aqui se define o objeto da classe testex e chamo o metodo do objeto
x=testex
x.metodox()
#aqui defino o objeto da classe testey e chamo o metodoy
x=testey
x.metodoy()
#aqui defino o objeto da classe testexy e chamo o metodox, o metodoy e o metodoxy
x=testexy
x.metodox()
x.metodoy()
x.metodoxy()
#obs:repare que eu usei a mesma variavel para ser o bjeto em todos
