
import random
def rolar_dados (n):
    i = 0
    lista = []
    while i<n:
        c = random.randint (1, 6)
        lista.append (c)
        i = i +1
    return lista

