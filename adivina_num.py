# Importamos el módulo 'random' para generar números pseudoaleatorios
import random

# Diccionario de configuración global para centralizar los parámetros de juego.
# Estructura de cada valor: (etiqueta legible, número máximo a adivinar, cantidad de vidas)
DIFICULTADES = {
    "1": ("Fácil (1-50)", 50, 10),
    "2": ("Medio (1-100)", 100, 7),
    "3": ("Difícil (1-200)", 200, 5)
}

def seleccionar_dificultad():
    """
    Muestra el menú de dificultades y valida la elección del usuario.
    Retorna una tupla: (rango_maximo, vidas).
    """
    print("Selecciona un nivel de dificultad:")
    # Iteramos sobre el diccionario para imprimir las opciones disponibles dinámicamente
    for clave, (nombre, _, vidas) in DIFICULTADES.items():
        print(f"[{clave}] {nombre} - {vidas} vidas")
    
    # Bucle de validación: no avanza hasta que la opción ingresada exista en el diccionario
    while True:
        opcion = input("Opción (1/2/3): ").strip()
        if opcion in DIFICULTADES:
            # Desempaquetamos los valores asociados a la clave elegida
            _, rango_max, vidas = DIFICULTADES[opcion]
            return rango_max, vidas
        print("Opción inválida. Intenta de nuevo.")

def jugar():
    """Controla la lógica principal de la partida y el flujo del juego."""
    print("=== ¡Bienvenido a 'Adivina el número'! ===")
    
    # Obtenemos la configuración según la dificultad seleccionada
    rango_max, vidas_restantes = seleccionar_dificultad()
    
    # Generamos el número secreto dentro del rango configurado (1 a rango_max)
    numero_secreto = random.randint(1, rango_max)
    intentos_realizados = 0

    print(f"\nHe elegido un número entre 1 y {rango_max}. Tienes {vidas_restantes} intentos.")

    # El ciclo principal corre mientras el jugador conserve vidas
    while vidas_restantes > 0:
        print(f"\nVidas restantes: {vidas_restantes}")
        entrada = input("Ingresa tu intento: ")

        # Manejo de excepciones para capturar valores que no se puedan convertir a int
        try:
            intento = int(entrada)
        except ValueError:
            print("Entrada no válida: por favor escribe un número entero.")
            # 'continue' evita descontar vidas si hubo un error de formato al escribir
            continue

        # Actualizamos las estadísticas tras una jugada válida
        intentos_realizados += 1
        vidas_restantes -= 1

        # Comparamos el valor ingresado con el número secreto
        if intento < numero_secreto:
            print("Más alto...")
        elif intento > numero_secreto:
            print("Más bajo...")
        else:
            # Condición de victoria: acierto antes de agotar vidas
            print(f"\n🎉 ¡Victoria! Acertaste el {numero_secreto} en {intentos_realizados} intentos.")
            return

    # Condición de derrota: el bucle terminó porque vidas_restantes llegó a 0
    print(f"\n💀 Fin del juego. Te quedaste sin intentos. El número era el {numero_secreto}.")

# Punto de entrada estándar para ejecutar el script directamente desde la consola
if __name__ == "__main__":
    jugar()