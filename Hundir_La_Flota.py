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
            
def colocar_barco_manual(tablero, tamaño_barco, numero_barco, tamaño_tablero):
    """Permite al jugador colocar un barco manualmente"""
    # Comentario: Encabezado visual para separar visualmente la colocación de cada barco
    print(f"\n{'='*50}")
    print(f"🚢 COLOCANDO BARCO {numero_barco} (Tamaño: {tamaño_barco})")
    print(f"{'='*50}")
    
    # Comentario: Muestra el tablero actual con coordenadas para que el jugador vea dónde colocar
    imprimir_tablero_con_coordenadas(tablero)
    
    # Comentario: Genera lista de letras (A, B, C...) según el tamaño del tablero para referencias
    letras_fila = [chr(65 + i) for i in range(tamaño_tablero)]
    
    # Comentario: Bucle infinito hasta que se coloque exitosamente el barco
    while True:
        # Comentario: Instrucciones para la orientación del barco
        print(f"\n📍 Coloca el barco de tamaño {tamaño_barco}")
        print("1. Horizontal (→)")
        print("2. Vertical (↓)")
        
        # Comentario: Valida que la entrada esté entre 1 y 2
        orientacion = obtener_entrada_valida(1, 2, "Selecciona la orientación (1-2): ")
        
        # Comentario: Bloque para barcos horizontales
        if orientacion == 1:
            print("\n Barco HORIZONTAL seleccionado")
            
            # Comentario: Obtiene el número de fila convertido de letra a índice numérico
            fila_num = obtener_coordenada_fila(tamaño_tablero)
            print(f"  Fila seleccionada: {letras_fila[fila_num]}")
            
            # Comentario: Calcula límite para columna inicial considerando el tamaño del barco
            col_inicio = obtener_entrada_valida(0, tamaño_tablero - tamaño_barco,
                                              f"Ingresa la columna inicial (0-{tamaño_tablero - tamaño_barco}): ")
            
            # Comentario: Verifica que todas las casillas necesarias estén libres (🌊)
            disponible = True
            for i in range(tamaño_barco):
                if tablero[fila_num][col_inicio + i] != "🌊":
                    print(f"❌ Error: La celda ({letras_fila[fila_num]}, {col_inicio + i}) ya está ocupada!")
                    disponible = False
                    break
            
            # Comentario: Si todas las casillas están libres, coloca el barco
            if disponible:
                for i in range(tamaño_barco):
                    tablero[fila_num][col_inicio + i] = "🚤"
                print(f"✅ Barco colocado en: {letras_fila[fila_num]}{col_inicio} a {letras_fila[fila_num]}{col_inicio + tamaño_barco - 1}")
                return True  # Comentario: Retorna True indicando éxito
            else:
                print("❌ No se puede colocar el barco ahí. Intenta otra ubicación.")
                
        # Comentario: Bloque para barcos verticales (misma lógica pero en vertical)
        else:  # Vertical
            print("\n📍 Barco VERTICAL seleccionado")
            
            # Comentario: Obtiene fila inicial con límite ajustado para que el barco no salga del tablero
            fila_inicio_num = obtener_coordenada_fila(tamaño_tablero - tamaño_barco)
            print(f"  Fila inicial seleccionada: {letras_fila[fila_inicio_num]}")
            
            # Comentario: Obtiene columna para barco vertical
            col = obtener_entrada_valida(0, tamaño_tablero - 1,
                                        f"Ingresa la columna (0-{tamaño_tablero-1}): ")
            
            # Comentario: Verifica disponibilidad en vertical
            disponible = True
            for i in range(tamaño_barco):
                if tablero[fila_inicio_num + i][col] != "🌊":
                    print(f"❌ Error: La celda ({letras_fila[fila_inicio_num + i]}, {col}) ya está ocupada!")
                    disponible = False
                    break
            
            # Comentario: Coloca barco vertical si hay espacio
            if disponible:
                for i in range(tamaño_barco):
                    tablero[fila_inicio_num + i][col] = "🚤"
                print(f"✅ Barco colocado en: {letras_fila[fila_inicio_num]}{col} a {letras_fila[fila_inicio_num + tamaño_barco - 1]}{col}")
                return True
            else:
                print("❌ No se puede colocar el barco ahí. Intenta otra ubicación.")

def colocar_barcos_manual(tablero, tamaño):
    """Permite al jugador colocar todos sus barcos manualmente"""
    # Comentario: Encabezado decorativo para la fase de colocación
    print("\n" + "⚓" * 17)
    print("⚓     COLOCACIÓN DE BARCOS     ⚓")
    print("⚓" * 17)
    
    # Comentario: Configuración de barcos según tamaño del tablero - reglas predefinidas
    if tamaño == 4:
        barcos = [2, 1]  # Un barco de 2 y uno de 1
    elif tamaño == 5:
        barcos = [3, 2, 1]
    elif tamaño == 6:
        barcos = [3, 2, 2, 1]
    elif tamaño == 7:
        barcos = [3, 3, 2, 1]
    elif tamaño == 8:
        barcos = [4, 3, 2, 2, 1]
    elif tamaño == 9:
        barcos = [4, 3, 3, 2, 1]
    elif tamaño == 10:
        barcos = [4, 3, 3, 2, 2, 1]
    else:
        # Comentario: Fórmula genérica para tamaños no predefinidos
        num_barcos = max(2, tamaño // 2)
        barcos = []
        for i in range(num_barcos):
            tamaño_barco = max(1, min(4, tamaño // 2 - i))
            barcos.append(tamaño_barco)
    
    # Comentario: Muestra resumen de barcos a colocar
    print(f"\n📊 Configuración de barcos para tablero {tamaño}x{tamaño}:")
    for i, tam in enumerate(barcos):
        print(f"  Barco {i+1}: {tam} casilla{'s' if tam > 1 else ''}")
    
    # Comentario: Instrucciones generales para el jugador
    print("\n📝 Ahora colocarás tus barcos en el tablero.")
    print("   Los barcos se representan con 🚤")
    print("   Usa coordenadas como 'A3', 'B5', etc.")
    print("   Las letras son filas, los números son columnas.")
    
    # Comentario: Bucle que coloca cada barco individualmente
    for i, tamaño_barco in enumerate(barcos):
        colocar_barco_manual(tablero, tamaño_barco, i+1, tamaño)
        print(f"\n✅ Barco {i+1} colocado exitosamente!")
    
    # Comentario: Mensaje final de éxito con decoración
    print("\n" + "✅" * 20)
    print("✅    TODOS LOS BARCOS COLOCADOS    ✅")
    print("✅" * 20)
    print("\nTu flota está lista para la batalla!")
    
    # Comentario: Muestra el tablero final completo
    print("\nTu tablero final:")
    imprimir_tablero(tablero)
    
    # Comentario: Pausa antes de comenzar el juego
    input("\nPresiona Enter para comenzar la batalla...")
    
   
def añadir_barcos_ia(tablero):

    """Coloca barcos de la IA automáticamente"""
    n = len(tablero)  # Obtiene el tamaño del tablero (n x n)

    # Determinar número y tamaño de barcos (igual que para el jugador)
    # Cada tamaño de tablero tiene una configuración específica de barcos
    if n == 4:
        barcos = [2, 1]  # Un barco de tamaño 2 y uno de tamaño 1
    elif n == 5:
        barcos = [3, 2, 1]
    elif n == 6:
        barcos = [3, 2, 2, 1]
    elif n == 7:
        barcos = [3, 3, 2, 1]
    elif n == 8:
        barcos = [4, 3, 2, 2, 1]
    elif n == 9:
        barcos = [4, 3, 3, 2, 1]
    elif n == 10:
        barcos = [4, 3, 3, 2, 2, 1]
    else:
        # Para tamaños personalizados calcula cuántos barcos poner
        num_barcos = max(2, n // 2)  # Mínimo 2 barcos
        barcos = []
        for i in range(num_barcos):
            # Calcula tamaño del barco entre 1 y 4
            tamaño_barco = max(1, min(4, n // 2 - i))
            barcos.append(tamaño_barco)
    
    # Intentar colocar cada barco en el tablero
    for tamaño_barco in barcos:
        colocado = False  # Indica si el barco ya fue colocado
        intentos = 0  # Evita bucles infinitos
        
        while not colocado and intentos < 100:  # Máximo 100 intentos
            vertical_horizontal = random.randint(1, 2)  # 1 = horizontal, 2 = vertical
            fila = random.randint(0, n - 1)  # Fila aleatoria
            col = random.randint(0, n - 1)  # Columna aleatoria

            # Intento de colocación horizontal
            if vertical_horizontal == 1:
                if col + tamaño_barco <= n:  # Verifica que el barco cabe
                    for i in range(tamaño_barco):
                        if tablero[fila][col + i] != "🌊":  # Si hay algo, no se puede colocar
                            break
                    else:
                        # Si no hubo break, coloca el barco
                        for i in range(tamaño_barco):
                            tablero[fila][col + i] = "🚤"
                        colocado = True

            # Intento de colocación vertical
            else:
                if fila + tamaño_barco <= n:  # Verifica que cabe verticalmente
                    for i in range(tamaño_barco):
                        if tablero[fila + i][col] != "🌊":
                            break
                    else:
                        for i in range(tamaño_barco):
                            tablero[fila + i][col] = "🚤"
                        colocado = True
            
            intentos += 1  # Incrementa intentos para evitar bucles infinitos


def seleccionar_celda(tablero, fila, columna):
    # Si hay un barco en la celda, es un impacto
    if tablero[fila][columna] == "🚤":
        tablero[fila][columna] = '💥'  # Marca impacto
        return True
    # Si hay agua, es un fallo
    elif tablero[fila][columna] == "🌊":
        tablero[fila][columna] = '💦'  # Marca agua
        return False
    else:
        # Si ya estaba marcada (💥 o 💦), no se puede volver a disparar
        return None
    

def condicion_victoria(tablero):
    # Recorre todas las filas buscando barcos
    for fila in tablero:
        if "🚤" in fila:  # Si queda un barco, no hay victoria
            return False
    return True  # No quedan barcos → victoria


def obtener_tamaño_tablero():
    """Permite al jugador elegir el tamaño del tablero"""
    # Muestra menú de selección
    print("\n" + "⚓" * 20)
    print("⚓  SELECCIÓN DEL TAMAÑO DEL TABLERO  ⚓")
    print("⚓" * 20)
    print("\nElige el tamaño del tablero:")
    print("1. Pequeño (4x4) - Recomendado para principiantes")
    print("2. Mediano (6x6) - Para jugadores intermedios")
    print("3. Grande (8x8) - Para expertos")
    print("4. Personalizado - Elige tu propio tamaño")
    
    # Pide opción válida
    opcion = obtener_entrada_valida(1, 4, "\nSelecciona una opción (1-4): ")
    
    # Devuelve tamaño según opción
    if opcion == 1:
        return 4
    elif opcion == 2:
        return 6
    elif opcion == 3:
        return 8
    else:
        # Tamaño personalizado
        print("\n" + "🔧" * 21)
        print("🔧     TAMAÑO PERSONALIZADO     🔧")
        print("🔧" * 21)
        print("\nNota: El tamaño mínimo es 4 y el máximo es 10.")
        tamaño = obtener_entrada_valida(4, 10, "Ingresa el tamaño del tablero (4-10): ")
        return tamaño


def jugar_barquitos():
    # Obtener el tamaño del tablero elegido por el jugador
    tamaño = obtener_tamaño_tablero()
    
    print(f"\n🔢 Has elegido un tablero de {tamaño}x{tamaño}")
    print(f"🎯 Preparando el juego...")
    
    # Crear tableros vacíos
    tablero_usuario = crear_tablero(tamaño, tamaño, "🌊")  # Tablero con barcos del jugador
    tablero_usuario_juego = crear_tablero(tamaño, tamaño, "🌊")  # Tablero donde se marcan disparos
    tablero_ia = crear_tablero(tamaño, tamaño, "🌊")  # Tablero de la IA
    
    # Colocar barcos del jugador manualmente
    colocar_barcos_manual(tablero_usuario, tamaño)
    
    # Colocar barcos de la IA automáticamente
    añadir_barcos_ia(tablero_ia)
    print("\n🤖 La IA ha colocado sus barcos secretamente...")

    turno = 1  # Contador de turnos

    # Bucle principal del juego
    while condicion_victoria(tablero_usuario) is False and condicion_victoria(tablero_ia) is False:

        # Mostrar información del turno
        print("\n" + "═" * (tamaño * 6))
        print(f"🔄 TURNO {turno}")
        print("═" * (tamaño * 6))

        # Mostrar tablero del jugador
        print("\n🚢 TU TABLERO DE JUEGO 🚢")
        imprimir_tablero(tablero_usuario)

        # Mostrar tablero donde el jugador dispara
        print("\n🎯 TABLERO DE ATAQUE 🎯")
        imprimir_tablero(tablero_usuario_juego)

        # TURNO DEL JUGADOR
        print("\n" + "─" * 35)
        print("🎮 TU TURNO")
        print(f"📍 Ingresa coordenadas como 'A0', 'B3', etc.")
        
        fila, columna = obtener_coordenada_jugador(tamaño)  # Pide coordenada válida
        letra_fila = chr(65 + fila)  # Convierte fila a letra
        print(f"  Disparando a: {letra_fila}{columna}")

        # Disparo del jugador
        resultado = seleccionar_celda(tablero_ia, fila, columna)

        if resultado is True:
            print("\n🎯 ¡IMPACTO! 💥")
            tablero_usuario_juego[fila][columna] = '💥'
        elif resultado is False:
            print("\n💧 AGUA")
            tablero_usuario_juego[fila][columna] = '💦'
        else:
            print("\n⚠️  Ya seleccionaste esa celda. Intenta de nuevo.")
            continue  # No cuenta turno

        # TURNO DE LA IA
        print("\n" + "─" * 35)
        print("🤖 TURNO DE LA IA")

        # IA elige coordenadas aleatorias
        fila_ia = random.randint(0, tamaño - 1)
        columna_ia = random.randint(0, tamaño - 1)

        resultado_ia = seleccionar_celda(tablero_usuario, fila_ia, columna_ia)

        # Mensajes según resultado
        if resultado_ia is True:
            print(f"🤖 La IA ha impactado en ({chr(65 + fila_ia)}{columna_ia}) 💥")
        elif resultado_ia is False:
            print(f"🤖 La IA ha fallado en ({chr(65 + fila_ia)}{columna_ia}) 💧")
        else:
            print(f"🤖 La IA ya seleccionó ({chr(65 + fila_ia)}{columna_ia})")
        
        turno += 1  # Avanza turno
    
    # FIN DEL JUEGO
    print("\n" + "═" * (tamaño * 6))
    print("🏁 FIN DEL JUEGO")
    print("═" * (tamaño * 6))
    
    print(f"\n📊 RESUMEN:")
    print(f"• Total de turnos: {turno - 1}")
    
    # Determinar ganador
    if condicion_victoria(tablero_ia):
        print("\n🎉 ¡FELICIDADES! HAS GANADO 🎉")
        print("🚤 Todos los barcos de la IA han sido hundidos! 💥")
        print("\n📜 TABLERO DE LA IA REVELADO:")
        imprimir_tablero(tablero_ia)
    else:
        print("\n😢 La IA ha ganado. Mejor suerte la próxima vez.")
        print("💥 La IA ha hundido todos tus barcos! 🚤")
        print("\n📜 TU TABLERO FINAL:")
        imprimir_tablero(tablero_usuario)
    
    # Preguntar si quiere jugar otra vez
    print("\n" + "♻️" * 25)
    jugar_otra = input("¿Quieres jugar otra vez? (s/n): ").lower()

    if jugar_otra == 's' or jugar_otra == 'si':
        print("\n" + "🔄" * 21)
        print("🔄     REINICIANDO EL JUEGO     🔄")
        print("🔄" * 21)
        jugar_barquitos()
    else:
        print("\n" + "👋" * 20)
        print("👋     ¡GRACIAS POR JUGAR!     👋")
        print("👋" * 20)


# Iniciar el juego
if __name__ == "__main__":
    # Mensaje de bienvenida
    print("\n" + "🌊" * 21)
    print("🌊🎮   BIENVENIDO A HUNDIR LA FLOTA   🎮🌊")
    print("🌊" * 21)
    print("\n📋 Leyenda:")
    print("🚤 = Barco")
    print("🌊 = Agua (sin descubrir)")
    print("💥 = Impacto (barco alcanzado)")
    print("💦 = Fallo (disparo al agua)")
    print("\n📌 Sistema de coordenadas:")
    print("   • Letras para filas (A, B, C, ...)")
    print("   • Números para columnas (0, 1, 2, ...)")
    print("   • Ejemplo: 'A0' es la esquina superior izquierda")
    
    jugar_barquitos()  # Inicia el juego
