import random
import os

# ==========================================
# UTILIDADES DE SISTEMA
# ==========================================

def limpiar_pantalla():
    # Borra todo lo que hay en la pantalla para que se vea limpio
    os.system('cls' if os.name == 'nt' else 'clear')

# ==========================================
# LÓGICA: HUNDIR LA FLOTA
# ==========================================

def crear_tablero_flota(filas, columnas, valor_inicial="🌊"):
    # Crea una lista de listas llena de olas de mar
    return [[valor_inicial for _ in range(columnas)] for _ in range(filas)]

def imprimir_tablero_flota(tablero):
    # Dibuja el tablero con barquitos pero sin las letras de los lados
    tamaño = len(tablero)
    ancho_celda = 5
    borde = "+" + "─" * ((ancho_celda - 1) * tamaño) + "+"
    print(borde)
    for fila in tablero:
        print("| " + " | ".join(fila) + " |")
        print(borde)

def imprimir_tablero_con_coordenadas_flota(tablero):
    # Dibuja el tablero con números arriba y letras al lado para poder apuntar
    tamaño = len(tablero)
    letras_fila = [chr(65 + i) for i in range(tamaño)]
    print("    ", end="")
    for col in range(tamaño):
        print(f"  {col}  " if col < 10 else f" {col}  ", end="")
    print("\n    +" + "─────" * tamaño + "+")
    for i in range(tamaño):
        print(f" {letras_fila[i]} |", end="")
        for j in range(tamaño):
            print(f" {tablero[i][j]} |", end="")
        print("\n    +" + "─────" * tamaño + "+")

def obtener_entrada_valida(min_v, max_v, msg):
    # Se asegura de que el usuario escriba un número correcto y no letras
    while True:
        try:
            v = int(input(msg))
            if min_v <= v <= max_v: return v
            print(f"Error: Número entre {min_v} y {max_v}")
        except ValueError: print("Error: Ingresa un número entero.")

def colocar_barcos_manual_flota(tablero, tamaño):
    # Decide cuántos barcos poner según lo grande que sea el tablero
    if tamaño == 4: barcos = [2, 1]
    elif tamaño == 5: barcos = [3, 2, 1]
    elif tamaño == 6: barcos = [3, 2, 2, 1]
    else: barcos = [4, 3, 2, 1]

    # Va pidiendo al usuario dónde poner cada barco uno por uno
    for i, tam_b in enumerate(barcos):
        while True:
            limpiar_pantalla()
            print(f"🚢 COLOCANDO BARCO {i+1} (Tamaño: {tam_b})")
            imprimir_tablero_con_coordenadas_flota(tablero)
            ori = obtener_entrada_valida(1, 2, "1. Horiz (→) | 2. Vert (↓): ")
            
            if ori == 1: # Si es horizontal
                f = ord(input("Fila (A, B...): ").upper()) - 65
                c = obtener_entrada_valida(0, tamaño - tam_b, f"Col de inicio (0-{tamaño-tam_b}): ")
                rango = [(f, c + j) for j in range(tam_b)]
            else: # Si es vertical
                f = obtener_entrada_valida(0, tamaño - tam_b, f"Fila de inicio (A=0, B=1...): ")
                c = obtener_entrada_valida(0, tamaño - 1, "Columna: ")
                rango = [(f + j, c) for j in range(tam_b)]
            
            # Mira si el sitio está libre antes de poner el barco
            if all(0 <= r[0] < tamaño and 0 <= r[1] < tamaño and tablero[r[0]][r[1]] == "🌊" for r in rango):
                for r in rango: tablero[r[0]][r[1]] = "🚤"
                break
            else: print("❌ Espacio inválido u ocupado.")

def jugar_hundir_la_flota():
    # Esta es la función principal que arranca el juego de los barcos
    limpiar_pantalla()
    print("⚓ --- HUNDIR LA FLOTA --- ⚓")
    tam = obtener_entrada_valida(4, 10, "Tamaño del tablero (4-10): ")
    tablero = crear_tablero_flota(tam, tam)
    colocar_barcos_manual_flota(tablero, tam)
    limpiar_pantalla()
    print("✅ ¡Flota lista!")
    imprimir_tablero_flota(tablero)
    input("\nPresiona Enter para volver al menú...")

# ==========================================
# LÓGICA: BUSCAMINAS
# ==========================================

victoria_bm = 0 # Cuenta cuántas casillas sin bomba hemos pisado

def tablero_base_bm(tablero_mostrar, columna):
    # Enseña el tablero tapado con cuadraditos negros que ve el jugador
    print("    ", end="")
    for i in range(columna):
        print(chr(65 + i), end="  ")
    print()
    for i in range(columna):
        print(f"{i + 1:<3}", end=" ")
        for j in range(columna):
            print(tablero_mostrar[i][j], end=" ")
        print()

def crear_tablero_interno_bm(minas, columna):
    # Crea el tablero secreto donde están las bombas de verdad
    tab = [[0 for _ in range(columna)] for _ in range(columna)]
    i = 0
    while i < minas:
        x, y = random.randint(0, columna-1), random.randint(0, columna-1)
        if tab[x][y] == 0:
            tab[x][y] = "*"
            i += 1
    # Pone los números indicando cuántas bombas hay cerca de cada casilla
    for i in range(columna):
        for j in range(columna):
            if tab[i][j] == "*":
                for ni in range(i-1, i+2):
                    for nj in range(j-1, j+2):
                        if 0 <= ni < columna and 0 <= nj < columna and tab[ni][nj] != "*":
                            tab[ni][nj] += 1
    return tab

def preguntar_coordenada_bm(tablero, tablero_mostrar, v_req):
    # Pide al usuario que elija una casilla y mira si ha explotado o no
    global victoria_bm
    entrada = input("Coordenadas (Ej: A1) o 'S' para salir: ").upper()
    if entrada == 'S': return False
    if len(entrada) < 2: return True
    
    col_idx = ord(entrada[0]) - 65
    try:
        fila_idx = int(entrada[1:]) - 1
        if tablero[fila_idx][col_idx] == "*":
            print("💥 ¡BOOM! Has perdido.")
            return False
        elif tablero_mostrar[fila_idx][col_idx] == "⬛️":
            tablero_mostrar[fila_idx][col_idx] = tablero[fila_idx][col_idx]
            victoria_bm += 1
            if victoria_bm == v_req:
                print("🏆 ¡VICTORIA!")
                return False
        return True
    except: return True

def jugar_buscaminas():
    # Función principal para jugar al Buscaminas
    global victoria_bm
    while True:
        limpiar_pantalla()
        print("💣 --- BUSCAMINAS --- 💣")
        print("1. Fácil | 2. Normal | 3. Difícil | 4. Salir")
        op = obtener_entrada_valida(1, 4, "Opción: ")
        if op == 4: break # Vuelve al menú de juegos
        
        # Ajustes de cada dificultad (tamaño, minas y puntos para ganar)
        datos = {1: (6, 6, 30), 2: (12, 50, 94), 3: (26, 200, 476)}
        col, minas, v_req = datos[op]
        victoria_bm = 0
        tab_m = [["⬛️" for _ in range(col)] for _ in range(col)]
        tab_r = crear_tablero_interno_bm(minas, col)
        
        # Bucle de la partida actual
        while True:
            limpiar_pantalla()
            tablero_base_bm(tab_m, col)
            if not preguntar_coordenada_bm(tab_r, tab_m, v_req): break
        input("Fin de la partida. Enter para volver...")

# ==========================================
# MENÚ PRINCIPAL
# ==========================================

def menu():
    # Este es el menú que ves al abrir el programa
    while True:
        limpiar_pantalla()
        print("================================")
        print("    🕹️  ARCADE PYTHON MULTIJUEGO")
        print("================================")
        print("1. 🚢 Hundir la Flota")
        print("2. 💣 Buscaminas")
        print("3. 🚪 Salir")
        print("--------------------------------")
        
        opcion = input("Elige tu desafío: ")
        
        if opcion == "1":
            jugar_hundir_la_flota() # Entra a los barcos
        elif opcion == "2":
            jugar_buscaminas() # Entra a las bombas
        elif opcion == "3":
            print("¡Gracias por jugar! 👋")
            break # Cierra el programa entero
        else:
            print("Opción no válida.")
            input("Enter para intentar de nuevo...")

if __name__ == "__main__":
    # Arranca el código llamando al menú principal
    menu()
