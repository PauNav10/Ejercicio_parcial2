import random

def jugar():
    numero_secreto = random.randint(1, 100)
    intentos = 0
    adivinado = False

    print("¡Bienvenido a 'Adivina el número'!")
    print("He elegido un número entre 1 y 100. ¿Puedes descubrir cuál es?")

    while not adivinado:
        entrada = input("\nIngresa tu intento: ")

        # Validamos que el usuario ingrese un número entero válido
        if not entrada.isdigit():
            print("Por favor, ingresa solo números enteros.")
            continue

        intento = int(entrada)
        intentos += 1

        if intento < numero_secreto:
            print("Más alto...")
        elif intento > numero_secreto:
            print("Más bajo...")
        else:
            adivinado = True
            print(f"¡Felicidades! Acertaste el número {numero_secreto} en {intentos} intentos.")

if __name__ == "__main__":
    jugar()