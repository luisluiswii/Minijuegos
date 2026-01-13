# 3 dificultades 6x6 (6) / 12x12 (50) / 26x26 (200)
import random

seguir = True
minas = 0
tablero = []


def coordenada():
    while True:
        coordenadas = input("Introduce la casilla")
        if len(coordenadas) == columna:
            return coordenadas
        else:
            print("Coordenadas no válidas. Intenta de nuevo")


def crear_tablero(minas, columna):
    # crea X minas en posiciones x e y

    for i in range(minas):
        posicion_mina_x = random.randint(0, columna)
        posicion_mina_y = random.randint(0, columna)

        if tablero(posicion_mina_x, posicion_mina_y) == 0:
            tablero(posicion_mina_x, posicion_mina_y) = "*"
        else:
            minas = minas + 1


def comprobar_minas():
    # si la mina es x e y necesitamos sumar alrededor
    # (x,y-1 x,y+1) (x-1,y-1 x-1,y x-1,y+1) (x+1,y-1 x+1,y x+1,y+1)
    if posicion == "*":
        # si encuentra una mina, sus posiciones alrededor + 1


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
            print("  ", end=" ")

            for i in range(5):
                print(chr(65 + i), end=" ")

            print(chr(65 + 6) + " ")

            for i in range(1, 6):
                print(i, "⬛️" * 6)

            crear_tablero(minas, columna)

        case 4:
            print("Saliendo del programa...")
            seguir = False

        case _:
            print("Error, opción no válida")
