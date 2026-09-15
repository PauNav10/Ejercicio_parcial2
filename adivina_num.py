# Importamos el módulo 'random' para generar números aleatorios
import random

# Diccionario con las configuraciones por nivel: (rango_maximo, vidas)
DIFICULTADES = {
    "1": ("Fácil (1-50)", 50, 10),
    "2": ("Medio (1-100)", 100, 7),
    "3": ("Difícil (1-200)", 200, 5)
}

def seleccionar_dificultad():
    """Permite al jugador elegir la dificultad antes de iniciar."""
    print("Selecciona un nivel de dificultad:")
    for clave, (nombre, _, vidas) in DIFICULTADES.items():
        print(f"[{clave}] {nombre} - {vidas} vidas")
    
    while True:
        opcion = input("Opción (1/2/3): ").strip()
        if opcion in DIFICULTADES:
            _, rango_max, vidas = DIFICULTADES[opcion]
            return rango_max, vidas
        print("Opción inválida. Intenta de nuevo.")

def jugar():
    print("=== ¡Bienvenido a 'Adivina el número'! ===")
    rango_max, vidas_restantes = seleccionar_dificultad()
    
    numero_secreto = random.randint(1, rango_max)
    intentos_realizados = 0

    print(f"\nHe elegido un número entre 1 y {rango_max}. Tienes {vidas_restantes} intentos.")

    # El juego continúa mientras queden vidas
    while vidas_restantes > 0:
        print(f"\nVidas restantes: {vidas_restantes}")
        entrada = input("Ingresa tu intento: ")

        # Manejo de excepciones para evitar que el programa truene con texto inválido
        try:
            intento = int(entrada)
        except ValueError:
            print("Entrada no válida: por favor escribe un número entero.")
            continue

        intentos_realizados += 1
        vidas_restantes -= 1

        if intento < numero_secreto:
            print("Más alto...")
        elif intento > numero_secreto:
            print("Más bajo...")
        else:
            print(f"\n ¡Victoria! Acertaste el {numero_secreto} en {intentos_realizados} intentos.")
            return

    # Si se agotan las vidas
    print(f"\n💀 Fin del juego. Te quedaste sin intentos. El número era el {numero_secreto}.")

if __name__ == "__main__":
    jugar()