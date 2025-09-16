"""
Scripts de ejemplo para diferentes casos de uso comunes
"""

import random
import string
from datetime import datetime, timedelta

def generador_passwords(longitud=8, incluir_simbolos=True):
    """Genera una contraseña aleatoria"""
    caracteres = string.ascii_letters + string.digits
    if incluir_simbolos:
        caracteres += "!@#$%&*"
    
    password = ''.join(random.choice(caracteres) for _ in range(longitud))
    return password

def validar_email(email):
    """Valida formato básico de email"""
    if "@" not in email:
        return False
    
    partes = email.split("@")
    if len(partes) != 2:
        return False
    
    usuario, dominio = partes
    if not usuario or not dominio:
        return False
    
    if "." not in dominio:
        return False
    
    return True

def calcular_edad(fecha_nacimiento):
    """Calcula la edad a partir de una fecha de nacimiento"""
    try:
        if isinstance(fecha_nacimiento, str):
            # Asume formato YYYY-MM-DD
            fecha_nacimiento = datetime.strptime(fecha_nacimiento, "%Y-%m-%d")
        
        hoy = datetime.now()
        edad = hoy.year - fecha_nacimiento.year
        
        # Ajustar si no ha pasado el cumpleaños este año
        if hoy.month < fecha_nacimiento.month or \
           (hoy.month == fecha_nacimiento.month and hoy.day < fecha_nacimiento.day):
            edad -= 1
        
        return edad
    except Exception as e:
        print(f"Error al calcular edad: {e}")
        return None

def convertir_temperatura(valor, de_escala, a_escala):
    """Convierte temperatura entre diferentes escalas"""
    # Normalizar las escalas
    de_escala = de_escala.lower()
    a_escala = a_escala.lower()
    
    # Convertir todo a Celsius primero
    if de_escala == "fahrenheit" or de_escala == "f":
        celsius = (valor - 32) * 5/9
    elif de_escala == "kelvin" or de_escala == "k":
        celsius = valor - 273.15
    elif de_escala == "celsius" or de_escala == "c":
        celsius = valor
    else:
        return "Escala de origen no válida"
    
    # Convertir desde Celsius a la escala destino
    if a_escala == "fahrenheit" or a_escala == "f":
        resultado = celsius * 9/5 + 32
    elif a_escala == "kelvin" or a_escala == "k":
        resultado = celsius + 273.15
    elif a_escala == "celsius" or a_escala == "c":
        resultado = celsius
    else:
        return "Escala de destino no válida"
    
    return round(resultado, 2)

def formatear_numero_telefono(numero):
    """Formatea un número de teléfono"""
    # Remover caracteres no numéricos
    numeros = ''.join(filter(str.isdigit, numero))
    
    if len(numeros) == 10:
        # Formato: (XXX) XXX-XXXX
        return f"({numeros[:3]}) {numeros[3:6]}-{numeros[6:]}"
    elif len(numeros) == 11 and numeros[0] == '1':
        # Formato con código de país: +1 (XXX) XXX-XXXX
        return f"+1 ({numeros[1:4]}) {numeros[4:7]}-{numeros[7:]}"
    else:
        return "Número de teléfono no válido"

def calcular_tiempo_transcurrido(fecha_inicio, fecha_fin=None):
    """Calcula el tiempo transcurrido entre dos fechas"""
    if fecha_fin is None:
        fecha_fin = datetime.now()
    
    if isinstance(fecha_inicio, str):
        fecha_inicio = datetime.fromisoformat(fecha_inicio)
    if isinstance(fecha_fin, str):
        fecha_fin = datetime.fromisoformat(fecha_fin)
    
    diferencia = fecha_fin - fecha_inicio
    
    dias = diferencia.days
    segundos = diferencia.seconds
    horas = segundos // 3600
    minutos = (segundos % 3600) // 60
    segundos = segundos % 60
    
    return {
        "dias": dias,
        "horas": horas,
        "minutos": minutos,
        "segundos": segundos,
        "total_segundos": diferencia.total_seconds()
    }

def generar_datos_prueba(cantidad=5):
    """Genera datos de prueba aleatorios"""
    nombres = ["Juan", "María", "Carlos", "Ana", "Luis", "Carmen", "Pedro", "Laura"]
    apellidos = ["García", "Rodríguez", "López", "Martínez", "Pérez", "González"]
    dominios = ["gmail.com", "yahoo.com", "hotmail.com", "empresa.com"]
    
    datos = []
    for i in range(cantidad):
        nombre = random.choice(nombres)
        apellido = random.choice(apellidos)
        email = f"{nombre.lower()}.{apellido.lower()}@{random.choice(dominios)}"
        edad = random.randint(18, 65)
        
        datos.append({
            "id": i + 1,
            "nombre": f"{nombre} {apellido}",
            "email": email,
            "edad": edad,
            "password": generador_passwords(10)
        })
    
    return datos

def menu_ejemplos():
    """Menú interactivo para probar los ejemplos"""
    while True:
        print("\n" + "="*50)
        print("EJEMPLOS DE SCRIPTS ÚTILES")
        print("="*50)
        print("1. Generar contraseña")
        print("2. Validar email")
        print("3. Calcular edad")
        print("4. Convertir temperatura")
        print("5. Formatear teléfono")
        print("6. Calcular tiempo transcurrido")
        print("7. Generar datos de prueba")
        print("8. Salir")
        
        opcion = input("\nElige una opción (1-8): ")
        
        if opcion == "1":
            longitud = input("Longitud de contraseña (8): ") or "8"
            simbolos = input("¿Incluir símbolos? (s/n): ").lower() == "s"
            password = generador_passwords(int(longitud), simbolos)
            print(f"Contraseña generada: {password}")
            
        elif opcion == "2":
            email = input("Ingresa un email: ")
            valido = validar_email(email)
            print(f"El email {'es válido' if valido else 'NO es válido'}")
            
        elif opcion == "3":
            fecha = input("Fecha de nacimiento (YYYY-MM-DD): ")
            edad = calcular_edad(fecha)
            if edad is not None:
                print(f"Edad: {edad} años")
                
        elif opcion == "4":
            valor = float(input("Valor de temperatura: "))
            de = input("Escala origen (C/F/K): ")
            a = input("Escala destino (C/F/K): ")
            resultado = convertir_temperatura(valor, de, a)
            print(f"Resultado: {resultado}")
            
        elif opcion == "5":
            telefono = input("Número de teléfono: ")
            formateado = formatear_numero_telefono(telefono)
            print(f"Formateado: {formateado}")
            
        elif opcion == "6":
            fecha = input("Fecha de inicio (YYYY-MM-DD HH:MM:SS): ")
            tiempo = calcular_tiempo_transcurrido(fecha)
            print(f"Tiempo transcurrido: {tiempo['dias']} días, {tiempo['horas']} horas, {tiempo['minutos']} minutos")
            
        elif opcion == "7":
            cantidad = input("¿Cuántos registros? (5): ") or "5"
            datos = generar_datos_prueba(int(cantidad))
            print("\nDatos generados:")
            for dato in datos:
                print(f"  {dato['id']}: {dato['nombre']} - {dato['email']} - {dato['edad']} años")
                
        elif opcion == "8":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida")

if __name__ == "__main__":
    menu_ejemplos()