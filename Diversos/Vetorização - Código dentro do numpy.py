import numpy as np
from timeit import Timer

# li = list(range(500000))
li = [1, 5, 7, 9, 13, 16, 20, 22, 26, 30, 31, 35, 40, 45, 42.3, 44, 47, 51.3, 52, 55, 59, 60, 60.1, 60.6, 65, 66]
nump_arr = np.array(li)


def python_for():
    for i in range(len(li)):
        li[i] + 5


def numpy_add():
    print((nump_arr * (9 / 5)) + 32)


# print(min(Timer(python_for).repeat(10, 10)))
print(min(Timer(numpy_add).repeat(10, 10)))

# R = int
# calc = [1, 5, 7, 9, 13, 16, 20, 22, 26, 30, 31, 35, 40, 45, 42.3, 44, 47, 51.3, 52, 55, 59, 60, 60.1, 60.6, 65, 66]
# sample = []
# for C in calc:
#     R = (C * (9 / 5)) + 32
#     sample.append(f'base.addSample(({C},),({R},))')
# MLP = '\n'.join(sample)
# arq = open('arquivos/Calc/MLP sample.txt', 'w')
# arq.write(MLP)
