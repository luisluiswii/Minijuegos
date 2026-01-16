# 3 dificultades 6x6 (6) / 12x12 (50) / 26x26 (200)
# total de casillas 1. 36(30) 2. 144(94) 3. 676 (476)

import random

seguir = True
minas = 0
columna = 0
tablero = []
tablero_mostrar = []
victoria = 0


# Muestra el tablero descuebirto
def print_tablero(tablero):
    for fila in tablero:
        for elemento in fila:
            print(elemento, end=" ")
        print()


# Muestra el tablero con el que se juega
def tablero_base(tablero_mostrar):
    print("    ", end="")

    # Imprimir letras de columnas
    for i in range(columna):
        print(chr(65 + i), end="  ")
    print()

    # Imprimir filas con números y el contenido de la matriz
    for i in range(columna):
        if i + 1 < 10:
            print(i + 1, end="  ")
        else:
            print(i + 1, end=" ")

        # Mostrar la fila i de la matriz tablero_mostrar
        for j in range(columna):
            print(tablero_mostrar[i][j], end=" ")
        print()


# Crea el trablero oculto por primera vez
def crear_tablero_cuadrados(tablero_mostrar, columna):
    for i in range(columna):
        fila = ["⬛️" for _ in range(columna)]
        tablero_mostrar.append(fila)

    return tablero_mostrar


# Rellena el tablero con las minas y el resto 0
def crear_tablero(minas, columna):
    tablero_local = []
    # Primero creamos el tablero con ceros
    for i in range(columna):
        fila = []
        for j in range(columna):
            fila.append(0)
        tablero_local.append(fila)

    # crea X minas en posiciones x e y
    i = 0
    while i < minas:
        posicion_mina_x = random.randint(0, columna - 1)
        posicion_mina_y = random.randint(0, columna - 1)

        if tablero_local[posicion_mina_x][posicion_mina_y] == 0:
            tablero_local[posicion_mina_x][posicion_mina_y] = "*"
            i += 1

    return tablero_local


# Actualiza el tablero respecto a las minas
def comprobar_minas(tablero, columna):
    # si la mina es x e y necesitamos sumar alrededor
    for i in range(columna):
        for j in range(columna):
            if tablero[i][j] == "*":
                # si encuentra una mina, sus posiciones alrededor + 1 pero solo si están dentro del tablero

                # arriba izquierda
                if i-1 >= 0 and j-1 >= 0 and tablero[i-1][j-1] != "*":
                    tablero[i-1][j-1] += 1

                # arriba
                if i-1 >= 0 and tablero[i-1][j] != "*":
                    tablero[i-1][j] += 1

                # arriba derecha
                if i-1 >= 0 and j+1 < columna and tablero[i-1][j+1] != "*":
                    tablero[i-1][j+1] += 1

                # izquierda
                if j-1 >= 0 and tablero[i][j-1] != "*":
                    tablero[i][j-1] += 1

                # derecha
                if j+1 < columna and tablero[i][j+1] != "*":
                    tablero[i][j+1] += 1

                # abajo izquierda
                if i+1 < columna and j-1 >= 0 and tablero[i+1][j-1] != "*":
                    tablero[i+1][j-1] += 1

                # abajo
                if i+1 < columna and tablero[i+1][j] != "*":
                    tablero[i+1][j] += 1

                # abajo derecha
                if i+1 < columna and j+1 < columna and tablero[i+1][j+1] != "*":
                    tablero[i+1][j+1] += 1


# Pregunta al usuario que coordenada pulsar y comprueba si hay mina
def preguntar_coordenada(tablero, tablero_mostrar, tablero_victoria):
    tamaño = len(tablero)

    coordenada_input = input("Introduce las Coordenadas (Letra/Número): ")

    if len(coordenada_input) >= 2:
        # Tomar la primera letra como columna
        letra = coordenada_input[0].upper()
        numero_str = coordenada_input[1:]

        if letra == "A":
            indice_columna = 0
        elif letra == "B":
            indice_columna = 1
        elif letra == "C":
            indice_columna = 2
        elif letra == "D":
            indice_columna = 3
        elif letra == "E":
            indice_columna = 4
        elif letra == "F":
            indice_columna = 5
        elif letra == "G":
            indice_columna = 6
        elif letra == "H":
            indice_columna = 7
        elif letra == "I":
            indice_columna = 8
        elif letra == "J":
            indice_columna = 9
        elif letra == "K":
            indice_columna = 10
        elif letra == "L":
            indice_columna = 11
        elif letra == "M":
            indice_columna = 12
        elif letra == "N":
            indice_columna = 13
        elif letra == "O":
            indice_columna = 14
        elif letra == "P":
            indice_columna = 15
        elif letra == "Q":
            indice_columna = 16
        elif letra == "R":
            indice_columna = 17
        elif letra == "S":
            indice_columna = 18
        elif letra == "T":
            indice_columna = 19
        elif letra == "U":
            indice_columna = 20
        elif letra == "V":
            indice_columna = 21
        elif letra == "W":
            indice_columna = 22
        elif letra == "X":
            indice_columna = 23
        elif letra == "Y":
            indice_columna = 24
        elif letra == "Z":
            indice_columna = 25
        else:
            print("Letra no válida")
            return True

        # Verificar que numero_str es un número
        if not numero_str.isdigit():
            print("Número no válido")
            return True

        indice_fila = int(numero_str) - 1

        if 0 <= indice_fila < tamaño and 0 <= indice_columna < tamaño:
            return comprobar(indice_fila, indice_columna, tablero, tablero_mostrar, tablero_victoria)
        else:
            print(
                f"Coordenadas fuera de rango. Tamaño máximo: {tamaño}x{tamaño}")
            return True
    else:
        print("Error de coordenada")
        return True


# Mediante las coordenadas comprueba si hay mina, si no actualiza el tablero que se muestra
def comprobar(indice_fila, indice_columna, tablero, tablero_mostrar, tablero_victoria):
    global victoria

    if tablero[indice_fila][indice_columna] == "*":
        print("Has perdido")
        print_tablero(tablero)
        return False
    else:
        tablero_mostrar[indice_fila][indice_columna] = tablero[indice_fila][indice_columna]
        victoria += 1

        if victoria == tablero_victoria:
            print("Has ganado")
            return False

        tablero_base(tablero_mostrar)
        return True


while (seguir):
    print("---------------------------")
    print("Bienvenido a Buscaminas")
    print("---------------------------")
    print("Seleccione una dificultad:")
    print(" ")
    print("1. Fácil (6x6)")
    print("2. Normal (12x12)")
    print("3. Difícil (26x26)")
    print("----------------------------")
    print("4. Salir")
    print(" ")

    opcion = int(input("Introduzca su opción:"))

    match(opcion):
        case 1:
            minas = 6
            columna = 6
            no_ganado = True
            tablero_victoria = 30
            victoria = 0

            tablero_mostrar = crear_tablero_cuadrados(tablero_mostrar, columna)
            tablero = crear_tablero(minas, columna)
            comprobar_minas(tablero, columna)
            tablero_base(tablero_mostrar)

            while no_ganado:
                no_ganado = preguntar_coordenada(
                    tablero, tablero_mostrar, tablero_victoria)

        case 2:
            minas = 50
            columna = 12
            no_ganado = True
            tablero_victoria = 94
            victoria = 0

            tablero_mostrar = crear_tablero_cuadrados(tablero_mostrar, columna)
            tablero = crear_tablero(minas, columna)
            comprobar_minas(tablero, columna)
            tablero_base(tablero_mostrar)

            while no_ganado:
                no_ganado = preguntar_coordenada(
                    tablero, tablero_mostrar, tablero_victoria)

        case 3:
            minas = 200
            columna = 26
            no_ganado = True
            tablero_victoria = 476
            victoria = 0

            tablero_mostrar = crear_tablero_cuadrados(tablero_mostrar, columna)
            tablero = crear_tablero(minas, columna)
            comprobar_minas(tablero, columna)
            tablero_base(tablero_mostrar)

            while no_ganado:
                no_ganado = preguntar_coordenada(
                    tablero, tablero_mostrar, tablero_victoria)

        case 4:
            print("Saliendo del programa...")
            seguir = False

        case _:
            print("Error, opción no válida")
