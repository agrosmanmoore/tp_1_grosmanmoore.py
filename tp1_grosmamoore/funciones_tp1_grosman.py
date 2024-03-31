import random
from termcolor import colored

n = 30  # NxN es el tamaño de la grilla
d = 0.6  # es la densidad del bosque
densidades=[0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]
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

def generar_bosque(d):
    """
    Genera una matriz que representa un bosque, donde los árboles están distribuidos aleatoriamente
    según la densidad d.

    Args:
        d (float): La densidad de árboles en el bosque.

    Returns:
        list: Una matriz que representa el bosque generado.
    """

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
    """
    Prende fuego en el medio del bosque.

    Args:
        bosque (list): La matriz que representa el bosque.

    Returns:
        None
    """

    arbolesmedio = ((n - 2) // 2)
    for i in range(arbolesmedio, arbolesmedio + 3):
        for j in range(arbolesmedio, arbolesmedio + 3):
            bosque[i][j] = 3

def imprimirbosque(av, aq, aqq, bosque,t):
    """
    Imprime el estado actual del bosque.

    Args:
        av (int): Número de árboles vivos.
        aq (int): Número de árboles prendidos.
        aqq (int): Número de árboles quemados.
        bosque (list): La matriz que representa el bosque.
        t (int): Tiempo transcurrido.

    Returns:
        None
    """

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
    """
    Reduce en uno el tiempo de quemado de los árboles prendidos.

    Args:
        bosque (list): La matriz que representa el bosque.

    Returns:
        list: La matriz actualizada que representa el bosque.
    """

    for i in range(n):
        for j in range(n):
            if bosque[i][j] > 0:
                bosque[i][j] -= 1
    return bosque

def quemando_alrededor(bosque, i, j):
    """
    Cuenta la cantidad de árboles prendidos alrededor de una posición en el bosque.

    Args:
        bosque (list): La matriz que representa el bosque.
        i (int): Índice de fila.
        j (int): Índice de columna.

    Returns:
        int: La cantidad de árboles prendidos alrededor.
    """

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
    """
    Propaga el fuego en el bosque.

    Args:
        bosque (list): La matriz que representa el bosque.

    Returns:
        None
    """

    probabilidad_quemado = 0
    for i in range(n):
        for j in range(n):
            if bosque[i][j] == -1:
                vecinos_quemando = quemando_alrededor(bosque, i, j)
                probabilidad_quemado = p[vecinos_quemando]
                if random.random() <= probabilidad_quemado:
                    bosque[i][j] = porquemar

def arboles_prendidos(bosque):
    """
    Cuenta el número de árboles prendidos en el bosque.

    Args:
        bosque (list): La matriz que representa el bosque.

    Returns:
        int: Número de árboles prendidos.
    """

    aq = 0
    for i in range(n):
        for j in range(n):
            if bosque[i][j] > 0:
                aq += 1
    return aq

def arboles_vivos(bosque):
    """
    Cuenta el número de árboles vivos en el bosque.

    Args:
        bosque (list): La matriz que representa el bosque.

    Returns:
        int: Número de árboles vivos.
    """
    av = 0
    for i in range(n):
        for j in range(n):
            if bosque[i][j] == -1:
                av += 1
    return av

def arboles_quemados(bosque):
    """
    Cuenta el número de árboles quemados en el bosque.

    Args:
        bosque (list): La matriz que representa el bosque.

    Returns:
        int: Número de árboles quemados.
    """

    aqq = 0
    for i in range(n):
        for j in range(n):
            if bosque[i][j] == 0:
                aqq += 1
    return aqq

def porquemarfuncion(bosque):
    """
    Cambia el estado de los árboles que están por quemarse.

    Args:
        bosque (list): La matriz que representa el bosque.

    Returns:
        None
    """

    for i in range(n):
        for j in range(n):
            if bosque[i][j] == -4:
                bosque[i][j] = 3

def simulaciondequemado(t):
    """
    Simula la propagación del fuego en el bosque.

    Args:
        t (int): Tiempo inicial.

    Returns:
        int: Tiempo transcurrido.
    """

    bosque = generar_bosque(d)
    prender_medio(bosque)
    

    while arboles_prendidos(bosque) > 0:
        t += 1
        propagacion(bosque)
        pasar_tiempo(bosque)
        porquemarfuncion(bosque)
    return t

def simulaciondequemado_densidad(d, t):
    """
    Simula la propagación del fuego en el bosque con una densidad específica.

    Args:
        d (float): Densidad de árboles.
        t (int): Tiempo inicial.

    Returns:
        float: Porcentaje de árboles quemados.
    """

    quemadostotal = 0
    vivosprincipio = 0
    
    bosque = generar_bosque(d)
    prender_medio(bosque)
    vivosprincipio = arboles_vivos(bosque)

    while arboles_prendidos(bosque) > 0:
        t += 1
        propagacion(bosque)
        pasar_tiempo(bosque)
        porquemarfuncion(bosque)
                
    quemadostotal = arboles_quemados(bosque)
    porcentaje = (quemadostotal / (vivosprincipio+9)) * 100
    
    return porcentaje

def porcentajepromedio():
    """
    Calcula el porcentaje promedio de árboles quemados para diferentes densidades.

    Returns:
        list: Lista de porcentajes promedio.
    """

    promedios = []
    for i in range(len(densidades)):
        d = densidades[i]
        sumaporcentajes = 0
        for j in range(100):
            sumaporcentajes += simulaciondequemado_densidad(d, t) 
        promedio = sumaporcentajes / 100
        promedios.append(promedio)
    return promedios

promedios = porcentajepromedio()

def imprimir_tabla_densidades():
    """
    Imprime una tabla con las densidades y el porcentaje promedio de árboles quemados.

    Returns:
        None
    """
    
    print("+----------+----------------+")
    print("| Densidad | Bosque quemado |")
    print("+----------+----------------+")


    for i in range(len(densidades)):
        d = densidades[i]
        promedio = promedios[i]
        
        d = str(round(d, 1))
        d_espacios = d + " " * (8 - len(d))

        promedio = str(round(promedio,2))
        promedio_espacios=promedio+" " * (6-len(promedio))
        
        print("| " + d_espacios + " | " + promedio_espacios  + " %       |")
        print("+----------+----------------+")


