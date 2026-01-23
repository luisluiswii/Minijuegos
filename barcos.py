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
                        
# Función para seleccionar una celda en el tablero del juego
def seleccionar_celda(tablero, fila, columna):
    """
    Procesa la selección de una celda en el tablero del juego.
    
    Parámetros:
    - tablero: matriz que representa el tablero de juego
    - fila: índice de la fila a seleccionar
    - columna: índice de la columna a seleccionar
    
    Retorna:
    - True: si se impactó un barco (celda con valor 1)
    - False: si fue agua (celda con valor "-")
    - None: si la celda ya fue seleccionada previamente
    """
    
    # Si la celda contiene un barco (representado por el número 1)
    if tablero[fila][columna] == 1:
        # Marcar como impacto con 'X'
        tablero[fila][columna] = 'X'
        return True  # Retorna True para indicar impacto exitoso
    
    # Si la celda está vacía (representada por "-")
    elif tablero[fila][columna] == "-":
        # Marcar como agua con 'O'
        tablero[fila][columna] = 'O'
        return False  # Retorna False para indicar que fue agua
    
    # Si la celda ya fue seleccionada anteriormente
    else:
        # Ya contiene 'X' o 'O', no se puede volver a seleccionar
        return None  # Retorna None para indicar celda ya usada


def condicion_victoria(tablero):
    """
    Verifica si se ha alcanzado la condición de victoria en el juego.
    
    Parámetros:
    - tablero: matriz que representa el tablero de juego
    
    Retorna:
    - True: si no quedan barcos por hundir (no hay más 1's en el tablero)
    - False: si aún quedan barcos por hundir
    """
    
    # Recorre cada fila del tablero
    for fila in tablero:
        # Si encuentra al menos un barco (número 1) en la fila
        if 1 in fila:
            return False  # Aún no hay victoria
    
    # Si recorrió todo el tablero y no encontró barcos
    return True  # ¡Victoria! Todos los barcos hundidos


def obtener_entrada_valida(tamaño, mensaje):
    """
    Solicita al usuario una entrada numérica válida dentro de un rango específico.
    
    Parámetros:
    - tamaño: número que define el límite superior (exclusivo) del rango permitido
    - mensaje: texto que se mostrará al usuario para solicitar la entrada
    
    Retorna:
    - valor: número entero válido ingresado por el usuario
    """
    
    # Bucle infinito hasta que el usuario ingrese un valor válido
    while True:
        try:
            # Solicitar entrada al usuario y convertirla a número entero
            valor = int(input(mensaje))
            
            # Verificar si el valor está dentro del rango permitido (0 a tamaño-1)
            if 0 <= valor < tamaño:
                return valor  # Retorna el valor válido
            else:
                # Mensaje de error si el número está fuera del rango
                print(f"Error: Debes ingresar un número entre 0 y {tamaño-1}. Intenta de nuevo.")
        
        except ValueError:
            # Captura error si el usuario ingresa algo que no es un número entero
            print("Error: Debes ingresar un número entero. Intenta de nuevo.")