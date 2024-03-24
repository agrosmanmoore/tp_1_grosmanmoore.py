import random
import termcolor
from termcolor import colored

def simulaciondequemado():

    n=30 # NxN es el tamaño de la grilla
    d=0.6 #es la densidad del bosque
    t=0
    p=[0,0.2,0.4,0.6,0.8,1,1,1,1]
    vacio=-2
    arbol="▓▓"
    arbolvivo=colored(arbol, "green")
    arbolquemando=colored(arbol, "red")
    arbolmuerto=colored(arbol, "white")
    av=0
    aq=0
    aqq=0
    porquemar=-4
    colorav=colored("Arboles vivos: ", "green")
    coloraq=colored("Arboles quemando: ", "red")
    coloraqq=colored("Arboles quemados: ", "grey")


    bosque=[]

    for i in range(n):
        fila=[]
        for j in range(n):
            fila+=[vacio]

            if random.random()<=d:
                fila[j]=-1

        bosque+=[fila]

    arbolesmedio= ((n-2) // 2)

    for i in range(arbolesmedio, arbolesmedio + 3):
        for j in range(arbolesmedio, arbolesmedio + 3):
            bosque[i][j] = 4

    def pasar_tiempo(bosque):
        for i in range(n):
            for j in range(n):
                if bosque[i][j] > 0:
                    bosque[i][j] -= 1
        return bosque

    def quemando_alrededor(bosque, i, j): 
        vecinos_quemando=0
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
        probabilidad_quemado=0
        for i in range(n):
            for j in range(n):
                if bosque[i][j] == -1:
                    vecinos_quemando = quemando_alrededor(bosque, i, j)
                    probabilidad_quemado = p[vecinos_quemando]
                    if random.random() <= probabilidad_quemado:
                        bosque[i][j] = porquemar
                    
    def arboles_prendidos(bosque):
        arbolesprendidos=0
        for i in range(n):
            for j in range(n):
                if bosque[i][j]>0:
                    arbolesprendidos+=1
        return arbolesprendidos

    def porquemarfuncion (bosque):
        for i in range(n):
            for j in range(n):
                if bosque[i][j] == -4:
                    bosque[i][j]=4

    while arboles_prendidos(bosque)>0:
        propagacion(bosque)
        porquemarfuncion(bosque)
        pasar_tiempo(bosque)
        t+=1
        
    return t

def tiempopromedio():
    tiempototal = 0
    for i in range(1000):
        tiempototal += simulaciondequemado()
    promedio = tiempototal / 1000
    return promedio

resultado = tiempopromedio()
print(f"Tiempo de quemado promedio en 1000 simulaciones: {resultado}")
