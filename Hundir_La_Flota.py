import random

def crear_tablero(filas, columnas, valor_inicial="🌊"):
    return [[valor_inicial for _ in range(columnas)] for _ in range(filas)]

def imprimir_tablero(tablero):
    """Imprime el tablero durante el juego - AHORA SIMÉTRICO"""
    tamaño = len(tablero)
    
    # Para emojis, necesitamos 2 caracteres para el contenido + espacios
    # Formato: "| 🌊 " donde el emoji ocupa 2 caracteres
    ancho_celda = 5  # "| " + emoji(2) + " " = 5 caracteres
    
    # Borde superior
    borde_superior = "+" + "─" * ((ancho_celda - 1) * tamaño) + "+"
    print(borde_superior)
    
    # Filas
    for i, fila in enumerate(tablero):
        fila_str = "|"
        for celda in fila:
            fila_str += f" {celda} |"
        print(fila_str)
        
        # Línea divisoria o borde inferior
        if i < tamaño - 1:
            print("+" + "─" * ((ancho_celda - 1) * tamaño) + "+")
        else:
            print("+" + "─" * ((ancho_celda - 1) * tamaño) + "+")

def imprimir_tablero_con_coordenadas(tablero):
    """Imprime el tablero con coordenadas - AHORA SIMÉTRICO Y CUADRADO"""
    tamaño = len(tablero)
    
    # Letras para las filas (A, B, C, ...)
    letras_fila = [chr(65 + i) for i in range(tamaño)]
    
    # Ancho de cada celda
    ancho_celda = 5  # "| 🌊 " donde el emoji ocupa 2 caracteres
    
    # 1. ENCABEZADO DE COLUMNAS (números centrados)
    # Espacio para la columna de letras (3 espacios)
    print("   ", end="")
    
    # Números de columnas centrados
    for col in range(tamaño):
        if col < 10:
            print(f"  {col}  ", end="")  # 2 espacios + número + 2 espacios
        else:
            print(f" {col}  ", end="")   # 1 espacio + número + 2 espacios
    print()
    
    # 2. BORDE SUPERIOR CON LETRAS DE FILA
    print("   +", end="")
    for _ in range(tamaño):
        print("─────", end="")  # 5 guiones por celda
    print("+")
    
    # 3. FILAS CON LETRAS Y CONTENIDO
    for i in range(tamaño):
        # Letra de la fila + borde izquierdo
        print(f" {letras_fila[i]} |", end="")
        
        # Contenido de las celdas
        for j in range(tamaño):
            print(f" {tablero[i][j]} |", end="")
        print()
        
        # LÍNEAS DIVISORIAS
        if i < tamaño - 1:
            print("   +", end="")
            for _ in range(tamaño):
                print("─────", end="")  # 5 guiones por celda
            print("+")
    
    # 4. BORDE INFERIOR
    print("   +", end="")
    for _ in range(tamaño):
        print("─────", end="")  # 5 guiones por celda
    print("+")