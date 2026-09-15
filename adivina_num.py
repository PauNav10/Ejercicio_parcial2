# Importamos el módulo 'random' para generar números aleatorios
import random

def jugar():
    # Genera un número entero aleatorio entre 1 y 100 (ambos inclusive)
    numero_secreto = random.randint(1, 100)
    
    # Contador para registrar cuántas veces prueba el jugador
    intentos = 0
    
    # Bandera booleana para controlar el estado del bucle del juego
    adivinado = False

    # Mensajes iniciales de bienvenida e instrucciones
    print("¡Bienvenido a 'Adivina el número'!")
    print("He elegido un número entre 1 y 100. ¿Puedes descubrir cuál es?")

    # El bucle se ejecutará indefinidamente hasta que 'adivinado' sea True
    while not adivinado:
        # Solicitamos la entrada del usuario por consola (siempre se recibe como texto/str)
        entrada = input("\nIngresa tu intento: ")

        # Validamos que la cadena contenga únicamente dígitos numéricos
        # Esto previene errores en tiempo de ejecución si el usuario escribe letras o símbolos
        if not entrada.isdigit():
            print("Por favor, ingresa solo números enteros.")
            # 'continue' salta el resto del código y regresa al inicio del bucle
            continue

        # Convertimos la entrada validada de texto (str) a número entero (int)
        intento = int(entrada)
        
        # Sumamos 1 al contador tras validar un intento correcto
        intentos += 1

        # Comparamos el intento del usuario con el número secreto
        if intento < numero_secreto:
            print("Más alto...")
        elif intento > numero_secreto:
            print("Más bajo...")
        else:
            # Si no es menor ni mayor, el usuario acertó
            adivinado = True
            # Mostramos el mensaje final interpolando las variables con un f-string
            print(f"¡Felicidades! Acertaste el número {numero_secreto} en {intentos} intentos.")

# Comprobamos si el script se está ejecutando directamente como programa principal
if __name__ == "__main__":
    jugar()