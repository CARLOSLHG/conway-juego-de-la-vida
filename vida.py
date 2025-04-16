import random
import time
import os
import sys
import csv

def pausar(mensaje="Presiona ENTER para continuar..."):
    input(f"\n{mensaje}")

def mostrar_readme():
    secciones = [
        """
JUEGO DE LA VIDA - INTRODUCCIÓN
════════════════════════════════
El Juego de la Vida es una simulación creada por John Conway en 1970.

No es un juego en el sentido tradicional (sin jugadores humanos). En su lugar,
es un experimento matemático donde las celdas viven, mueren o nacen en función
de reglas simples.

A través de generaciones, pueden surgir patrones como criaturas que se mueven,
oscilan o incluso se replican.
        """,

        """
REGLAS DEL JUEGO
═════════════════
1. Supervivencia: Una celda viva con 2 o 3 vecinas vive.
2. Soledad: Una celda viva con menos de 2 vecinas muere.
3. Sobrepoblación: Una celda viva con más de 3 vecinas muere.
4. Nacimiento: Una celda muerta con exactamente 3 vecinas vivas nace.

A partir de estas reglas surgen estructuras fascinantes y caóticas.
        """,

        """
¿QUÉ HACE ESTE SCRIPT?
═══════════════════════
Este script en Python permite simular el Juego de la Vida en la terminal.
Puedes configurar:

- Tamaño del mundo (ancho y alto)
- Probabilidad de vida inicial (solo en modo random)
- Número máximo de generaciones
- Velocidad del ciclo
- Patrón inicial (random, glider, lwss, blinker, toad)
- Exportación a .txt o .csv si lo deseas
        """,

        """
USO DEL SCRIPT
═══════════════
python vida.py <ancho> <alto> <prob_vida> <max_generaciones> <delay> <patron> [--export_txt salida.txt] [--export_csv salida.csv]

Ejemplo:
python vida.py 40 20 0.3 100 0.2 glider --export_txt salida.txt --export_csv salida.csv
        """,

        """
PATRONES INCLUIDOS
═══════════════════
- random → generación aleatoria
- glider → nave diagonal
- lwss → nave espacial horizontal
- blinker → oscilador lineal
- toad → oscilador 2x3

¡Puedes observar cómo se comportan a lo largo del tiempo!
        """
    ]

    for seccion in secciones:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(seccion)
        pausar()

    # Opción de ejecución directa
    os.system('cls' if os.name == 'nt' else 'clear')
    print("¿Deseas comenzar el juego con tus propios parámetros ahora?")
    respuesta = input("Escribe S para sí, o cualquier otra tecla para salir: ").strip().lower()

    if respuesta == 's':
        iniciar_interactivamente()
    else:
        print("\n¡Gracias por explorar el Juego de la Vida!\n")
        sys.exit(0)

def iniciar_interactivamente():
    try:
        width = int(input("Ancho del grid: "))
        height = int(input("Alto del grid: "))
        prob = float(input("Probabilidad inicial de vida (0.0 - 1.0): "))
        max_gens = int(input("Máximo de generaciones (-1 para infinito): "))
        delay = float(input("Delay entre generaciones (en segundos): "))
        pattern = input("Patrón (random, glider, lwss, blinker, toad): ").strip()

        export_txt = input("¿Exportar a TXT? (deja vacío si no): ").strip()
        export_csv = input("¿Exportar a CSV? (deja vacío si no): ").strip()

        run_game(width, height, prob, max_gens, delay, pattern, export_txt or None, export_csv or None)

    except Exception as e:
        print(f"[ERROR] Entrada inválida: {e}")
        sys.exit(1)

# Funciones anteriores...
def parse_args():
    if '--readme' in sys.argv:
        mostrar_readme()

    if len(sys.argv) < 7 or sys.argv[1] in ['--help', '-h']:
        mostrar_ayuda()

    width = int(sys.argv[1])
    height = int(sys.argv[2])
    prob = float(sys.argv[3])
    max_gens = int(sys.argv[4])
    delay = float(sys.argv[5])
    pattern = sys.argv[6]

    export_txt = None
    export_csv = None

    if '--export_txt' in sys.argv:
        export_txt = sys.argv[sys.argv.index('--export_txt') + 1]
    if '--export_csv' in sys.argv:
        export_csv = sys.argv[sys.argv.index('--export_csv') + 1]

    return width, height, prob, max_gens, delay, pattern, export_txt, export_csv

def mostrar_ayuda():
    print("""
═════════════════════════════════════════════════
JUEGO DE LA VIDA - PYTHON
═════════════════════════════════════════════════

Uso:
python vida.py <ancho> <alto> <prob_vida> <max_generaciones> <delay> <patron> [--export_txt archivo.txt] [--export_csv archivo.csv]

También puedes ejecutar:
python vida.py --readme   ← para aprender antes de jugar
════════════════════════════════════════════════════
""")
    sys.exit(0)

# --- FUNCIONES DE JUEGO (misma lógica anterior) ---
def create_grid_random(width, height, prob):
    return [[random.random() < prob for _ in range(width)] for _ in range(height)]

def empty_grid(width, height):
    return [[False for _ in range(width)] for _ in range(height)]

def insert_pattern(grid, pattern_coords, offset_x, offset_y):
    for dx, dy in pattern_coords:
        x, y = dx + offset_x, dy + offset_y
        if 0 <= x < len(grid) and 0 <= y < len(grid[0]):
            grid[x][y] = True

def create_pattern_grid(width, height, pattern):
    grid = empty_grid(width, height)
    mid_x = height // 2 - 2
    mid_y = width // 2 - 2

    patterns = {
        'glider': [(1, 2), (2, 3), (3, 1), (3, 2), (3, 3)],
        'lwss': [(1, 1), (1, 4), (2, 0), (3, 0), (4, 0), (4, 4), (2, 5), (3, 5)],
        'blinker': [(2, 1), (2, 2), (2, 3)],
        'toad': [(2, 2), (2, 3), (2, 4), (3, 1), (3, 2), (3, 3)],
    }

    insert_pattern(grid, patterns[pattern], mid_x, mid_y)
    return grid

def count_neighbors(grid, x, y):
    height, width = len(grid), len(grid[0])
    directions = [(-1, -1), (-1, 0), (-1, 1),
                  (0, -1),         (0, 1),
                  (1, -1),  (1, 0), (1, 1)]
    return sum(1 for dx, dy in directions
               if 0 <= x + dx < height and 0 <= y + dy < width and grid[x + dx][y + dy])

def next_generation(grid):
    height, width = len(grid), len(grid[0])
    return [[(grid[i][j] and count_neighbors(grid, i, j) in [2, 3]) or
             (not grid[i][j] and count_neighbors(grid, i, j) == 3)
             for j in range(width)] for i in range(height)]

def print_grid(grid, gen):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"Generación {gen}")
    for row in grid:
        print("".join(['■' if cell else ' ' for cell in row]))

def export_txt(file, grids):
    with open(file, 'w') as f:
        for gen, grid in enumerate(grids):
            f.write(f"Generación {gen}\n")
            for row in grid:
                f.write("".join(['■' if cell else ' ' for cell in row]) + "\n")
            f.write("\n")

def export_csv(file, grids):
    with open(file, 'w', newline='') as f:
        writer = csv.writer(f)
        for gen, grid in enumerate(grids):
            writer.writerow([f"Generación {gen}"])
            writer.writerows([[1 if cell else 0 for cell in row] for row in grid])
            writer.writerow([])

def run_game(width, height, prob, max_gens, delay, pattern, export_txt_path, export_csv_path):
    grid = create_grid_random(width, height, prob) if pattern == 'random' else create_pattern_grid(width, height, pattern)

    generation = 0
    history = []

    while max_gens == -1 or generation < max_gens:
        print_grid(grid, generation)
        history.append(grid)
        grid = next_generation(grid)
        generation += 1
        time.sleep(delay)

    if export_txt_path:
        export_txt(export_txt_path, history)
    if export_csv_path:
        export_csv(export_csv_path, history)

# Punto de entrada principal
if __name__ == "__main__":
    args = parse_args()
    run_game(*args)
