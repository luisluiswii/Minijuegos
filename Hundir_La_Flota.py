import random

def crear_tablero(filas, columnas, valor_inicial="🌊"):
    return [[valor_inicial for _ in range(columnas)] for _ in range(filas)]

def imprimir_tablero(tablero):
    """Imprime el tablero durante el juego"""
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
    """Imprime el tablero con coordenadas"""
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
            print("\n📍 Barco HORIZONTAL seleccionado")
            
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
