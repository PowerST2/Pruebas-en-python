"""
Ejemplos básicos de Python para aprender conceptos fundamentales
"""

# 1. Variables y tipos de datos
def variables_ejemplo():
    """Ejemplo de variables y tipos de datos"""
    print("=== Variables y Tipos de Datos ===")
    nombre = "Python"
    edad = 30
    altura = 1.75
    es_programador = True
    
    print(f"Nombre: {nombre} (tipo: {type(nombre).__name__})")
    print(f"Edad: {edad} (tipo: {type(edad).__name__})")
    print(f"Altura: {altura} (tipo: {type(altura).__name__})")
    print(f"Es programador: {es_programador} (tipo: {type(es_programador).__name__})")

# 2. Listas y operaciones básicas
def listas_ejemplo():
    """Ejemplo de listas y sus operaciones"""
    print("\n=== Listas ===")
    frutas = ["manzana", "banana", "naranja"]
    print(f"Lista original: {frutas}")
    
    frutas.append("uva")
    print(f"Después de agregar uva: {frutas}")
    
    frutas.remove("banana")
    print(f"Después de quitar banana: {frutas}")
    
    print(f"Primera fruta: {frutas[0]}")
    print(f"Número de frutas: {len(frutas)}")

# 3. Bucles simples
def bucles_ejemplo():
    """Ejemplo de bucles for y while"""
    print("\n=== Bucles ===")
    
    # Bucle for
    print("Contando del 1 al 5:")
    for i in range(1, 6):
        print(f"Número: {i}")
    
    # Bucle while
    print("Contando hacia atrás:")
    contador = 5
    while contador > 0:
        print(f"Cuenta atrás: {contador}")
        contador -= 1

# 4. Funciones básicas
def saludo(nombre="Mundo"):
    """Función que saluda"""
    return f"¡Hola, {nombre}!"

def calculadora_simple(a, b, operacion):
    """Calculadora simple"""
    if operacion == "+":
        return a + b
    elif operacion == "-":
        return a - b
    elif operacion == "*":
        return a * b
    elif operacion == "/":
        return a / b if b != 0 else "Error: División por cero"
    else:
        return "Operación no válida"

def main():
    """Ejecuta todos los ejemplos"""
    variables_ejemplo()
    listas_ejemplo()
    bucles_ejemplo()
    
    print("\n=== Funciones ===")
    print(saludo())
    print(saludo("Python"))
    
    print("\n=== Calculadora ===")
    print(f"5 + 3 = {calculadora_simple(5, 3, '+')}")
    print(f"10 - 4 = {calculadora_simple(10, 4, '-')}")
    print(f"6 * 7 = {calculadora_simple(6, 7, '*')}")
    print(f"15 / 3 = {calculadora_simple(15, 3, '/')}")

if __name__ == "__main__":
    main()