
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

def remover_dado(rol, guar, n):
    i = 0
    novoguar = []
    
    while i < len(guar):
        if i != n:
            novoguar.append(guar[i])
        i = i + 1

    novorol = rol.copy()
    novorol.append(guar[n])

    return [novorol, novoguar]

def calcula_pontos_regra_simples (d):
    resultado = {}
    f = 1
    while f<=6:
        soma = 0
        i = 0

        while i<len(d):
            if d[i] ==f:
                soma = soma + d[i]
            i = i +1

        resultado[f] = soma
        f = f +1

    return resultado