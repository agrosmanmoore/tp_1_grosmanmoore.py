import random
import termcolor
from termcolor import colored
from funciones_tp1_grosman import *

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

def tiempopromedio():
    tiempototal = 0
    for i in range(1000):
        tiempototal += simulaciondequemado(t)
    promedio = tiempototal / 1000

    return promedio
promedio=tiempopromedio()

print(f"Tiempo de quemado promedio en 1000 simulaciones: {promedio}")
