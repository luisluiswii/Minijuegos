import random

def añadir_barcos(tablero):
    n = len(tablero)
    numero_de_barcos = random.randint(1, n) # Aquí definimos  el numero de barcos que va a tener la partida siendo un numero random entre 1 y n
    
    for num in range(numero_de_barcos):
        
        tamaño_barco= random.randint(1,min(n// 2, 4))# Crea un tamaño aleatorio entre 1 y el valor más pequeño entre n//2 y 4
        
        colocado = False #Creamos un colocado fase para el while que se repita tantas veces hasta que esten colocados todos los barcos
        
        while not colocado:
            vertical_horizontal = random.randint(1, 2)
            fila = random.randint(0, n -1)
            col = random.randint(0, n -1) #lo colocamos en una posicion aleatoria de vertical y horizontal entre 0 y el largo y ancho del tablero