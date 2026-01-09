# 3 dificultades 6x6 / 12x12 / 26x26
seguir = True

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
            print("   " + "A" + " " + "B" + " " + "C" +
                  " " + "D" + " " + "E" + " " + "F")

            for i in range(1, 6):
                print(i, "⬛️" * 6)

        case 2:
            print("   ", end=" ")

            for i in range(25):
                print(chr(65 + i), end=" ")

            print(chr(65 + 25) + " ")

            for i in range(1, 27):
                if i < 10:
                    print(f"0{i} {'⬛️' * 26}")

                if i >= 10:
                    print(i, "⬛️" * 26)

        case 3:
            print("   ", end=" ")

            for i in range(11):
                print(chr(65 + i), end=" ")

            print(chr(65 + 12) + " ")

            for i in range(1, 13):
                if i < 10:
                    print(f"0{i} {'⬛️' * 12}")

                if i >= 10:
                    print(i, "⬛️" * 12)

        case 4:
            print("Saliendo del programa...")
            seguir = False

        case _:
            print("Error, opción no válida")
