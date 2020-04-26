# Vetorização é uma tecnica para trabalhar com numeros e loops com a biblioteca numpy, que é mais rapida
import numpy as np
from timeit import Timer

li = list(range(500000))
nump_arr = np.array(li)

def python_for():
    return [num + 1 for num in li]

def numpy_add():
    return nump_arr + 1

print(min(Timer(python_for).repeat(10, 10)))
print(min(Timer(numpy_add).repeat(10, 10)))