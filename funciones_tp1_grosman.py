import random
from termcolor import colored

n = 30  # NxN es el tamaño de la grilla
d = 0.6  # es la densidad del bosque
t = 0
p = [0, 0.2, 0.4, 0.6, 0.8, 1, 1, 1, 1]
vacio = -2
arbol = "▓▓"
arbolvivo = colored(arbol, "green")
arbolquemando = colored(arbol, "red")
arbolmuerto = colored(arbol, "white")
av = 0
aq = 0
aqq = 0
porquemar = -4
colorav = colored("Arboles vivos: ", "green")
coloraq = colored("Arboles quemando: ", "red")
coloraqq = colored("Arboles quemados: ", "grey")

def generar_bosque():
    bosque = []

    for i in range(n):
        fila = []
        for j in range(n):
            fila.append(vacio)

            if random.random() <= d:
                fila[j] = -1

        bosque.append(fila)
        
    return bosque

def prender_medio(bosque):
    arbolesmedio = ((n - 2) // 2)
    for i in range(arbolesmedio, arbolesmedio + 3):
        for j in range(arbolesmedio, arbolesmedio + 3):
            bosque[i][j] = 3

def imprimirbosque(av, aq, aqq, bosque):
    for fila in bosque:
        for elem in fila:
            if elem == -1:
                print(arbolvivo, end="")
            elif elem == 0:
                print(arbolmuerto, end="")
            elif elem >= 1:
                print(arbolquemando, end="")
            else:
                print("  ", end="")
        print()
    print(f"Tiempo transcurrido: {t} \n{colorav}{arboles_vivos(bosque)} \n{coloraq}{arboles_prendidos(bosque)} \n{coloraqq}{arboles_quemados(bosque)}")

def pasar_tiempo(bosque):
    for i in range(n):
        for j in range(n):
            if bosque[i][j] > 0:
                bosque[i][j] -= 1
    return bosque

def quemando_alrededor(bosque, i, j): 
    vecinos_quemando = 0
    if i + 1 < n and j + 1 < n and bosque[i+1][j+1] > 0:
        vecinos_quemando += 1
    if i + 1 < n and bosque[i+1][j] > 0:
        vecinos_quemando += 1
    if i + 1 < n and j - 1 >= 0 and bosque[i+1][j-1] > 0:
        vecinos_quemando += 1
    if j + 1 < n and bosque[i][j+1] > 0:
        vecinos_quemando += 1
    if j - 1 >= 0 and bosque[i][j-1] > 0:
        vecinos_quemando += 1
    if i - 1 >= 0 and j + 1 < n and bosque[i-1][j+1] > 0:
        vecinos_quemando += 1
    if i - 1 >= 0 and bosque[i-1][j] > 0:
        vecinos_quemando += 1
    if i - 1 >= 0 and j - 1 >= 0 and bosque[i-1][j-1] > 0:
        vecinos_quemando += 1
    return vecinos_quemando

def propagacion(bosque):
    probabilidad_quemado = 0
    for i in range(n):
        for j in range(n):
            if bosque[i][j] == -1:
                vecinos_quemando = quemando_alrededor(bosque, i, j)
                probabilidad_quemado = p[vecinos_quemando]
                if random.random() <= probabilidad_quemado:
                    bosque[i][j] = porquemar

def arboles_prendidos(bosque):
    aq = 0
    for i in range(n):
        for j in range(n):
            if bosque[i][j] > 0:
                aq += 1
    return aq

def arboles_vivos(bosque):
    av = 0
    for i in range(n):
        for j in range(n):
            if bosque[i][j] == -1:
                av += 1
    return av

def arboles_quemados(bosque):
    aqq = 0
    for i in range(n):
        for j in range(n):
            if bosque[i][j] == 0:
                aqq += 1
    return aqq

def porquemarfuncion(bosque):
    for i in range(n):
        for j in range(n):
            if bosque[i][j] == -4:
                bosque[i][j] = 3
