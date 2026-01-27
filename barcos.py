import random


def crear_tablero(filas, columnas, valor_inicial="-"):  # Crea la matriz tablero
    tablero = []  # Crea el tablero vacio
    for _ in range(filas):
        # Crea las filas poniendo tantos caracteres como columnas vayamos a poner
        fila = [valor_inicial] * columnas
        # Añade las filas al tablero creando por filas el tablero
        tablero.append(fila)
    return tablero


def imprimir_tablero(tablero):  # Genera el tablero
    for fila in tablero:
        # Genera los separadores entre columnas introduciendo "|" entre cada elemento de la fila. Con el .join los va introduciendo detras de cada caracter.
        print(" | ".join(fila))
        # Genera los separadores entre filas. Para ajustar todos los caracteres usamos la formula y * 4 + 3 siendo "y" la cantidad de caracteres.
        print("-" * (len(fila) * 4 - 3))


def añadir_barcos(tablero):
    n = len(tablero)
    # Aquí definimos  el numero de barcos que va a tener la partida siendo un numero random entre 1 y n
    numero_de_barcos = random.randint(1, n)

    for num in range(numero_de_barcos):

        # Crea un tamaño aleatorio entre 1 y el valor más pequeño entre n//2 y 4
        tamaño_barco = random.randint(1, min(n // 2, 4))

        colocado = False  # Creamos un colocado fase para el while que se repita tantas veces hasta que esten colocados todos los barcos

        while not colocado:
            vertical_horizontal = random.randint(1, 2)
            fila = random.randint(0, n - 1)
            # lo colocamos en una posicion aleatoria de vertical y horizontal entre 0 y el largo y ancho del tablero
            col = random.randint(0, n - 1)

            if vertical_horizontal == 1:  # Horizontal
                if col + tamaño_barco <= n:  # col + tamaño_barco <= n significa: "posición inicial + tamaño del barco no se sale del tablero"
                    # Verifica que todas las celdas necesarias estén VACÍAS ("-")
                    for i in range(tamaño_barco):
                        # Revisa cada celda: tablero[fila][col + i]
                        # Si encuentra una celda ocupada (diferente de "-"), rompe el ciclo
                        if tablero[fila][col + i] != "-":
                            break
                    else:
                        for i in range(tamaño_barco):
                            # Marca cada celda con 1 (barco colocado)
                            tablero[fila][col + i] = 1
                        colocado = True  # Indica que el barco fue colocado exitosamente

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
                            # Marca cada celda con 1
                            tablero[fila + i][col] = 1
                        colocado = True  # Indica que el barco fue colocado exitosamente

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
                print(
                    f"Error: Debes ingresar un número entre 0 y {tamaño-1}. Intenta de nuevo.")

        except ValueError:
            # Captura error si el usuario ingresa algo que no es un número entero
            print("Error: Debes ingresar un número entero. Intenta de nuevo.")


def jugar_barquitos(tamaño):
    """
    Función principal que ejecuta el juego de los barquitos (Hundir la flota/Battleship).

    Parámetros:
    - tamaño: dimensión del tablero (tamaño x tamaño)
    """

    # 1. CREACIÓN DEL TABLERO DEL USUARIO (JUGADOR)
    # Crea un tablero vacío para el usuario con las dimensiones especificadas
    tablero_usuario = crear_tablero(tamaño, tamaño)

    # Añade barcos aleatoriamente al tablero del usuario
    añadir_barcos(tablero_usuario)

    # 2. CREACIÓN DEL TABLERO DE JUEGO DEL USUARIO
    # Este tablero muestra solo los disparos realizados por el usuario
    # Inicialmente está vacío (todo con "-"), representa lo que el usuario ve del oponente
    tablero_usuario_juego = crear_tablero(tamaño, tamaño, "-")

    # 3. CREACIÓN DEL TABLERO DE LA INTELIGENCIA ARTIFICIAL (IA)
    # Crea un tablero vacío para la IA con las mismas dimensiones
    tablero_ia = crear_tablero(tamaño, tamaño)

    # Añade barcos aleatoriamente al tablero de la IA
    añadir_barcos(tablero_ia)

    # 4. BUCLE PRINCIPAL DEL JUEGO
    # El juego continúa mientras ambos jugadores tengan barcos sin hundir
    while condicion_victoria(tablero_usuario) is False and condicion_victoria(tablero_ia) is False:
        """
        Condición del bucle:
        - condicion_victoria(tablero_usuario) = False → El usuario aún tiene barcos
        - condicion_victoria(tablero_ia) = False → La IA aún tiene barcos
        - El bucle se ejecuta mientras AMBOS sigan teniendo barcos
        - El juego termina cuando UNO de los dos ya no tiene barcos
        """

        # 5. MOSTRAR INFORMACIÓN AL USUARIO

        # a) Mostrar el tablero del usuario (con sus barcos y los disparos recibidos)
        print("Tu tablero de juego :\n")
        imprimir_tablero(tablero_usuario)
        # Muestra: barcos propios ('1'), impactos recibidos ('X'), agua recibida ('O')

        # b) Mostrar el tablero de ataque del usuario
        print("Tablero de juego del ataque :\n")
        imprimir_tablero(tablero_usuario_juego)
        # Muestra: disparos realizados contra la IA ('X', 'O', '-')
        # No muestra los barcos de la IA, solo los resultados de los disparos

        # NOTA: El código continúa aquí (se omitió parte posterior del bucle)
        # Normalmente aquí seguiría:
        # 1. Turno del usuario para atacar
        # 2. Turno de la IA para atacar
        # 3. Verificar si alguien ganó

        print("\n--- Tu turno ---")  # Empieza el turno del jugador

        # Pedimos la celda en la que quiere disparar nuestro usuario
        fila = obtener_entrada_valida(tamaño, f"Dime la fila (0-{tamaño-1})")
        columna = obtener_entrada_valida(
            tamaño, f"Dime la columna (0-{tamaño-1})")
        # Y si coincide con el tablero de la ia en la fila y la columna sabremos si impacto o no o si repitio casilla
        resultado = seleccionar_celda(tablero_ia, fila, columna)

        if resultado is True:
            print("¡Impacto!")
            tablero_usuario_juego[fila][columna] = 'X'
        elif resultado is False:
            print("¡Agua!")
            # Aqui 'pintamos  el diparo ya sea con X o 0 depende de el resultado'
            tablero_usuario_juego[fila][columna] = '0'
        else:
            print("Ya disparaste en esta celda antes.")

        print("\n--- Turno de la IA ---")

        fila_ia = random.randint(0, tamaño - 1)  # Genera fila de la IA
        columna_ia = random.randint(0, tamaño - 1)  # Genera columna de la IA
        # Genera el resultado de la IA
        resultado_ia = seleccionar_celda(tablero_usuario, fila_ia, columna_ia)

        # Comprobacion de la IA para saber si acierta o es agua
        if resultado_ia is True:
            # Acierta el disparo
            print(f"La IA ha impactado en ({fila_ia}, {columna_ia})")
        elif resultado_ia is False:
            # Falla el disparo
            print(f"La IA ha fallado en ({fila_ia}, {columna_ia})")
        else:
            # La IA ha hecho un disparo en una casilla que ya habia sido atacada en otro turno
            print(
                f"La IA ya seleccionó ({fila_ia}, {columna_ia}). Intenta de nuevo.")
            
            
    # Verificar quién ganó
    # Esta sección evalúa el resultado final del juego
    if condicion_victoria(tablero_ia):
    # Si la función condicion_victoria devuelve True al pasarle el tablero de la IA
    # Significa que el jugador humano ha ganado (ha hundido todos los barcos de la IA)
        print("\n¡Felicidades! Has ganado.")
    
    else:
    # Si condicion_victoria devuelve False
    # Significa que la IA ha ganado (el jugador no pudo hundir todos los barcos)
        print("\nLa IA ha ganado. Mejor suerte la próxima vez.")

# Iniciar el juego
# Llama a la función principal que ejecuta todo el juego
# El parámetro 4 indica el tamaño del tablero (probablemente 4x4)
jugar_barquitos(4)