import random
from termcolor import colored
from funciones_tp1_grosman import *

n = 30  # NxN es el tamaño de la grilla
densidades = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]
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

imprimir_tabla_densidades()