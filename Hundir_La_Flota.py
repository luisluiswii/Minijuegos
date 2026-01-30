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

def convertir_coordenada_letra_a_numero(letra):
    """Convierte una letra (A, B, C, ...) a número (0, 1, 2, ...)"""
    if len(letra) != 1 or not letra.isalpha():  # Verifica que sea solo un carácter alfabético
        return None  # Retorna None si la entrada no es válida
    return ord(letra.upper()) - 65  # Convierte la letra mayúscula a número (A=0, B=1, etc.)

def obtener_entrada_valida(min_valor, max_valor, mensaje):
    """Obtiene una entrada válida del usuario dentro del rango permitido"""
    while True:  # Bucle infinito hasta obtener una entrada válida
        try:
            valor = int(input(mensaje))  # Solicita y convierte a entero
            if min_valor <= valor <= max_valor:  # Verifica que esté en el rango
                return valor  # Retorna el valor si es válido
            else:
                print(f"Error: Debes ingresar un número entre {min_valor} y {max_valor}. Intenta de nuevo.")
        except ValueError:  # Captura error si no se puede convertir a entero
            print("Error: Debes ingresar un número entero. Intenta de nuevo.")

def obtener_coordenada_fila(tamaño_tablero):
    """Obtiene una coordenada de fila (letra) válida"""
    letras_validas = [chr(65 + i) for i in range(tamaño_tablero)]  # Genera lista de letras válidas
    
    while True:  # Bucle hasta obtener una fila válida
        entrada = input(f"Ingresa la letra de la fila ({letras_validas[0]}-{letras_validas[-1]}): ").strip().upper()
        
        if len(entrada) == 1 and entrada.isalpha():  # Verifica que sea un solo carácter alfabético
            fila_num = convertir_coordenada_letra_a_numero(entrada)  # Convierte letra a número
            if fila_num is not None and 0 <= fila_num < tamaño_tablero:  # Verifica que esté en rango
                return fila_num  # Retorna el número de fila
            else:
                print(f"Error: La letra debe estar entre {letras_validas[0]} y {letras_validas[-1]}")
        else:
            print("Error: Debes ingresar una sola letra")

def obtener_coordenada_jugador(tamaño):
    """Obtiene coordenadas del jugador durante el juego"""
    letras_validas = [chr(65 + i) for i in range(tamaño)]  # Genera lista de letras válidas
    
    while True:  # Bucle hasta obtener coordenadas válidas
        entrada = input(f"Ingresa coordenada (ej: {letras_validas[0]}0, B3): ").strip().upper()
        
        if len(entrada) >= 2:  # Verifica que tenga al menos 2 caracteres
            letra = entrada[0]  # Toma el primer carácter como letra
            numero_str = entrada[1:]  # Toma el resto como número en string
            
            if letra.isalpha() and numero_str.isdigit():  # Verifica que letra sea alfabética y número sea dígitos
                fila = convertir_coordenada_letra_a_numero(letra)  # Convierte letra a número
                columna = int(numero_str)  # Convierte string a entero
                
                if fila is not None and 0 <= fila < tamaño and 0 <= columna < tamaño:  # Verifica rangos
                    return fila, columna  # Retorna tupla con coordenadas
                else:
                    print(f"Error: Coordenada fuera de rango. Usa letras {letras_validas[0]}-{letras_validas[-1]} y números 0-{tamaño-1}")
            else:
                print("Error: Formato incorrecto. Usa formato como 'A0', 'B3', etc.")
        else:
            print("Error: Entrada demasiado corta. Usa formato como 'A0', 'B3', etc.")