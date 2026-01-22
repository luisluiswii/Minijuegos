import random

def crear_tablero(filas, columnas, valor_inicial="-"): # Crea la matriz tablero
    tablero = [] # Crea el tablero vacio
    for _ in range(filas):
        fila = [valor_inicial] * columnas # Crea las filas poniendo tantos caracteres como columnas vayamos a poner
        tablero.append(fila) # Añade las filas al tablero creando por filas el tablero
    return tablero

def imprimir_tablero(tablero): # Genera el tablero
    for fila in tablero:
        print(" | ".join(fila)) # Genera los separadores entre columnas introduciendo "|" entre cada elemento de la fila. Con el .join los va introduciendo detras de cada caracter.
        print("-" * (len(fila) * 4 - 3)) # Genera los separadores entre filas. Para ajustar todos los caracteres usamos la formula y * 4 + 3 siendo "y" la cantidad de caracteres.



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




            if vertical_horizontal == 1:  # Horizontal
                if col + tamaño_barco <= n: #col + tamaño_barco <= n significa: "posición inicial + tamaño del barco no se sale del tablero"
                    for i in range(tamaño_barco): # # Verifica que todas las celdas necesarias estén VACÍAS ("-")
                        # Revisa cada celda: tablero[fila][col + i]
                        # Si encuentra una celda ocupada (diferente de "-"), rompe el ciclo
                        if tablero[fila][col + i] != "-":
                            break
                    else:
                        for i in range(tamaño_barco):
                            # Marca cada celda con 1 (barco colocado)
                            tablero[fila][col + i] = 1
                        colocado = True # Indica que el barco fue colocado exitosamente

            else:  # Vertical
                if fila + tamaño_barco <= n:  # fila + tamaño_barco <= n significa: "fila inicial + tamaño del barco no se sale del tablero"
                    for i in range(tamaño_barco):
                        # Revisa cada celda: tablero[fila + i][col]
                        # Si encuentra una celda ocupada, rompe el ciclo
                        if tablero[fila + i][col] != "-":
                            break
                    else:
                        # Coloca el barco verticalmente
                        for i in range(tamaño_barco):
                            tablero[fila + i][col] = 1 # Marca cada celda con 1
                        colocado = True # Indica que el barco fue colocado exitosamente