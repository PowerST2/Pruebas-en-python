"""
Script interactivo para practicar entrada de datos del usuario
"""

def obtener_datos_usuario():
    """Obtiene datos básicos del usuario"""
    print("=== Información Personal ===")
    nombre = input("¿Cuál es tu nombre? ")
    edad = input("¿Cuántos años tienes? ")
    
    try:
        edad = int(edad)
        if edad >= 18:
            print(f"Hola {nombre}, eres mayor de edad ({edad} años)")
        else:
            print(f"Hola {nombre}, eres menor de edad ({edad} años)")
    except ValueError:
        print(f"Hola {nombre}, no pude entender tu edad")

def juego_adivinanza():
    """Juego simple de adivinanza"""
    import random
    
    print("\n=== Juego de Adivinanza ===")
    numero_secreto = random.randint(1, 10)
    intentos = 3
    
    print("He pensado un número entre 1 y 10. ¡Adivínalo!")
    
    while intentos > 0:
        try:
            guess = int(input(f"Intento {4-intentos}/3: "))
            
            if guess == numero_secreto:
                print("¡Felicidades! ¡Adivinaste!")
                break
            elif guess < numero_secreto:
                print("El número es mayor")
            else:
                print("El número es menor")
                
            intentos -= 1
            
            if intentos == 0:
                print(f"¡Se acabaron los intentos! El número era {numero_secreto}")
                
        except ValueError:
            print("Por favor, ingresa un número válido")

def calculadora_interactiva():
    """Calculadora que pide datos al usuario"""
    print("\n=== Calculadora Interactiva ===")
    
    try:
        num1 = float(input("Primer número: "))
        operacion = input("Operación (+, -, *, /): ")
        num2 = float(input("Segundo número: "))
        
        if operacion == "+":
            resultado = num1 + num2
        elif operacion == "-":
            resultado = num1 - num2
        elif operacion == "*":
            resultado = num1 * num2
        elif operacion == "/":
            if num2 != 0:
                resultado = num1 / num2
            else:
                print("Error: No se puede dividir por cero")
                return
        else:
            print("Operación no válida")
            return
            
        print(f"Resultado: {num1} {operacion} {num2} = {resultado}")
        
    except ValueError:
        print("Error: Ingresa números válidos")

def main():
    """Función principal con menú"""
    while True:
        print("\n" + "="*40)
        print("SCRIPTS INTERACTIVOS")
        print("="*40)
        print("1. Información personal")
        print("2. Juego de adivinanza")
        print("3. Calculadora")
        print("4. Salir")
        
        opcion = input("\nElige una opción (1-4): ")
        
        if opcion == "1":
            obtener_datos_usuario()
        elif opcion == "2":
            juego_adivinanza()
        elif opcion == "3":
            calculadora_interactiva()
        elif opcion == "4":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    main()