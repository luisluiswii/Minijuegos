# 3 dificultades 6x6 (6) / 12x12 (50) / 26x26 (200)
import random

seguir = True
minas = 0
columna = 0
tablero = []


def print_tablero(tablero):
    for fila in tablero:
        for elemento in fila:
            print(elemento, end=" ")
        print()


def tablero_base():
    print("    ", end="")

    # Imprimir letras de columnas
    for i in range(columna):
        print(chr(65 + i), end=" ")
    print()

    # Imprimir filas con números y casillas vacías
    for i in range(1, columna + 1):
        if i < 10:
            print(i, end="  ")
        else:
            print(i, end=" ")
        print("⬛️" * columna)


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


def preguntar_coordenada(tablero, no_ganar):
    coordenada_input = input("Introduce las Coordenadas (Letra/Número): ")

    if len(coordenada_input) >= 2:
        # Tomar la primera letra como columna
        letra = coordenada_input[0].upper()
        numero = coordenada_input[1:]

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

        if tablero[indice_columna, numero] == "*":
            no_ganar = False
            print("Has perdido")
            print_tablero(tablero)
    else:
        print("Error de coordenada")


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

            tablero = crear_tablero(minas, columna)
            comprobar_minas(tablero, columna)
            tablero_base()

            while no_ganado:
                preguntar_coordenada(no_ganado)

        case 2:
            minas = 50
            columna = 12

            tablero = crear_tablero(minas, columna)
            comprobar_minas(tablero, columna)
            tablero_base()
            # print_tablero(tablero)

        case 3:
            minas = 200
            columna = 26

            tablero = crear_tablero(minas, columna)
            comprobar_minas(tablero, columna)
            # print_tablero(tablero)
            tablero_base()

        case 4:
            print("Saliendo del programa...")
            seguir = False

        case _:
            print("Error, opción no válida")
