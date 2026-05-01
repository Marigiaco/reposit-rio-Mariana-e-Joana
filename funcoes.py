
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

def calcula_pontos_soma (l):
    i = 0
    soma = 0
    while i<len(l):
        soma = soma + l[i]
        i = i +1
    return soma

def calcula_pontos_sequencia_baixa (l):
    m = []
    i = 1
    while i<=3:
        if i in l and i+1 in l and i+2 in l and i+3 in l:
            return 15
        i = i+1
    return 0

def calcula_pontos_sequencia_alta (l):
    i = 1
    while i<=2:
        if i in l and i+1 in l and i+2 in l and i+3 in l and i+4 in l:
            return 30
        i = i +1
    return 0

def calcula_pontos_full_house (l):
    i = 0
    soma = 0
    while i<len(l):
        soma = soma + l[i]
        i = i +1
    contagens = {}
    i = 0
    while i<len(l):
        valor = l[i]
        if valor in contagens:
            contagens[valor] = contagens[valor] +1
        else:
            contagens[valor] = 1
        i = i +1

    tres = False
    dois = False

    for valor in contagens:
        if contagens[valor] == 3:
            tres = True
        elif contagens[valor] == 2:
            dois = True

    if tres and dois:
        return soma
    else:
        return 0


def calcula_pontos_quadra (l):
    c = []
    for i in range(1,7):
        q = 0
        for n in l:
            if n ==i:
                q = q +1
        if q>=4:
            soma=0
            for n in l:
                soma = soma +n
            return soma
    return 0

def calcula_pontos_quina (l):
    c = []
    for i in range (1,7):
        q = 0
        for n in l:
            if n ==i:
                q = q +1
        if q>=5:
            return 50
    return 0

def calcula_pontos_regra_avancada(faces):
    dic = {}
    dic['cinco_iguais'] = calcula_pontos_quina(faces)
    dic['full_house'] = calcula_pontos_full_house(faces)
    dic['quadra'] = calcula_pontos_quadra(faces)
    dic['sem_combinacao'] = calcula_pontos_soma(faces)
    dic['sequencia_alta'] = calcula_pontos_sequencia_alta(faces)
    dic['sequencia_baixa'] = calcula_pontos_sequencia_baixa(faces)

    return dic

def faz_jogada(dados,categoria,cartela_de_pontos):

    if categoria in cartela_de_pontos['regra_avancada']:
        pontos_a = calcula_pontos_regra_avancada(dados)
        cartela_de_pontos['regra_avancada'][categoria] = pontos_a[categoria]
    else:
        categoria_int = int(categoria)
        pontos_s = calcula_pontos_regra_simples(dados)
        cartela_de_pontos['regra_simples'][categoria_int] = pontos_s[categoria_int]
    
    return cartela_de_pontos

def imprime_cartela(cartela):
    print("Cartela de Pontos:")
    print("-"*25)    
    for i in range(1, 7):
        filler = " " * (15 - len(str(i)))
        if cartela['regra_simples'][i] != -1:
            print(f"| {i}: {filler}| {cartela['regra_simples'][i]:02} |")
        else:
            print(f"| {i}: {filler}|    |")
    for i in cartela['regra_avancada'].keys():
        filler = " " * (15 - len(str(i)))
        if cartela['regra_avancada'][i] != -1:
            print(f"| {i}: {filler}| {cartela['regra_avancada'][i]:02} |")
        else:
            print(f"| {i}: {filler}|    |")
    print("-"*25)

    

    
     
        



