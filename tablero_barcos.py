
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