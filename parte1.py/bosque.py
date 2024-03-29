import random
from termcolor import colored
from funciones_tp1_grosman import *

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

bosque = generar_bosque()
prender_medio(bosque)
imprimirbosque(av, aq, aqq, bosque)

while arboles_prendidos(bosque) > 0:
    t += 1
    propagacion(bosque)
    pasar_tiempo(bosque)
    porquemarfuncion(bosque)
    imprimirbosque(av, aq, aqq, bosque)
