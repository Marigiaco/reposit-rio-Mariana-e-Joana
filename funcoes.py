
import random
def rolar_dados (n):
    i = 0
    lista = []
    while i<n:
        c = random.randint (1, 6)
        lista.append (c)
        i = i +1
    return lista


def guardar_dado (drol, dguar, n):
    m = []
    restantes = []
    i = 0
    while i<len(dguar):
        m.append(dguar[i])
        i = i +1
    m.append(drol[n])
    i = 0
    while i<len(drol):
        if i != n:
            restantes.append(drol[i])
        i = i +1

    resultado = [restantes, m]
    return resultado
