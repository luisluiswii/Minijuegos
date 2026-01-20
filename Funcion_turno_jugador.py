    # Turno del jugador - con validación de entrada
""" print("\n--- Tu turno ---")
    fila = obtener_entrada_valida(tamaño, f"Selecciona la fila (0-{tamaño-1}): ")
    columna = obtener_entrada_valida(tamaño, f"Selecciona la columna (0-{tamaño-1}): ")

    resultado = seleccionar_celda(tablero_ia, fila, columna)
    if resultado is True:
        print("¡Impacto!")
        tablero_usuario_juego[fila][columna] = 'X'
    elif resultado is False:
        print("Agua.")
        tablero_usuario_juego[fila][columna] = 'O'
    else:
        print("Ya seleccionaste esa celda. Intenta de nuevo.") Luis"""
print("\n--- Tu turno ---") #Empieza el turno del jugador
fila = obtener_entrada_valida(tamaño,f"Dime la fila (0-{tamaño-1})") #Pedimos la celda en la que quiere disparar nuestro usuario
columna = obtener_entrada_valida(tamaño,f"Dime la columna (0-{tamaño-1})")
resultado = seleccionar_celda(tablero_ia,fila, columna) #Y si coincide con el tablero de la ia en la fila y la columna sabremos si impacto o no o si repitio casilla
if resultado is True:
    print ("¡Impacto!")
    tablero_usuario_juego[fila] [columna] = 'X'
elif resultado is False:
    print("¡Agua!")
    tablero_usuario_juego[fila] [columna] = '0' #Aqui 'pintamos  el diparo ya sea con X o 0 depende de el resultado'
else: 
    print("Ya disparaste en esta celda antes.")