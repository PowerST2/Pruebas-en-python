"""
Scripts de nivel intermedio: Manipulación de archivos
"""

import os
import json
import csv
from datetime import datetime

def leer_archivo_texto(archivo):
    """Lee un archivo de texto y muestra su contenido"""
    try:
        with open(archivo, 'r', encoding='utf-8') as f:
            contenido = f.read()
            print(f"Contenido de {archivo}:")
            print("-" * 30)
            print(contenido)
            print("-" * 30)
            print(f"El archivo tiene {len(contenido)} caracteres")
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo {archivo}")
    except Exception as e:
        print(f"Error al leer el archivo: {e}")

def escribir_archivo_texto(archivo, contenido):
    """Escribe contenido en un archivo de texto"""
    try:
        with open(archivo, 'w', encoding='utf-8') as f:
            f.write(contenido)
        print(f"Contenido escrito en {archivo}")
    except Exception as e:
        print(f"Error al escribir el archivo: {e}")

def contar_palabras_archivo(archivo):
    """Cuenta palabras en un archivo"""
    try:
        with open(archivo, 'r', encoding='utf-8') as f:
            contenido = f.read()
            palabras = contenido.split()
            lineas = contenido.split('\n')
            
        print(f"Estadísticas de {archivo}:")
        print(f"- Líneas: {len(lineas)}")
        print(f"- Palabras: {len(palabras)}")
        print(f"- Caracteres: {len(contenido)}")
        
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo {archivo}")

def trabajar_con_json():
    """Ejemplos de trabajo con archivos JSON"""
    datos = {
        "nombre": "Script de prueba",
        "version": "1.0",
        "fecha": datetime.now().isoformat(),
        "configuracion": {
            "debug": True,
            "idioma": "es"
        },
        "numeros": [1, 2, 3, 4, 5]
    }
    
    # Escribir JSON
    archivo_json = "temp_config.json"
    with open(archivo_json, 'w', encoding='utf-8') as f:
        json.dump(datos, f, indent=2, ensure_ascii=False)
    
    print(f"Archivo JSON creado: {archivo_json}")
    
    # Leer JSON
    with open(archivo_json, 'r', encoding='utf-8') as f:
        datos_leidos = json.load(f)
    
    print("Datos leídos del JSON:")
    for clave, valor in datos_leidos.items():
        print(f"  {clave}: {valor}")
    
    # Limpiar archivo temporal
    os.remove(archivo_json)
    print("Archivo temporal eliminado")

def trabajar_con_csv():
    """Ejemplos de trabajo con archivos CSV"""
    archivo_csv = "temp_datos.csv"
    
    # Datos de ejemplo
    empleados = [
        {"nombre": "Juan", "edad": 30, "departamento": "IT"},
        {"nombre": "María", "edad": 25, "departamento": "HR"},
        {"nombre": "Carlos", "edad": 35, "departamento": "Finance"},
        {"nombre": "Ana", "edad": 28, "departamento": "IT"}
    ]
    
    # Escribir CSV
    with open(archivo_csv, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=["nombre", "edad", "departamento"])
        writer.writeheader()
        writer.writerows(empleados)
    
    print(f"Archivo CSV creado: {archivo_csv}")
    
    # Leer CSV
    print("Datos del CSV:")
    with open(archivo_csv, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for fila in reader:
            print(f"  {fila['nombre']} - {fila['edad']} años - {fila['departamento']}")
    
    # Limpiar archivo temporal
    os.remove(archivo_csv)
    print("Archivo temporal eliminado")

def listar_archivos_directorio(directorio="."):
    """Lista archivos en un directorio"""
    try:
        print(f"Archivos en {os.path.abspath(directorio)}:")
        for item in os.listdir(directorio):
            ruta_completa = os.path.join(directorio, item)
            if os.path.isfile(ruta_completa):
                size = os.path.getsize(ruta_completa)
                print(f"  📄 {item} ({size} bytes)")
            elif os.path.isdir(ruta_completa):
                print(f"  📁 {item}/")
    except Exception as e:
        print(f"Error al listar directorio: {e}")

def crear_archivo_log():
    """Crea un archivo de log simple"""
    archivo_log = "actividad.log"
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    mensaje = f"[{timestamp}] Script ejecutado correctamente\n"
    
    with open(archivo_log, 'a', encoding='utf-8') as f:
        f.write(mensaje)
    
    print(f"Entrada agregada al log: {archivo_log}")

def main():
    """Función principal para demostrar manipulación de archivos"""
    print("=== MANIPULACIÓN DE ARCHIVOS ===\n")
    
    # Crear archivo de ejemplo
    archivo_ejemplo = "ejemplo.txt"
    contenido_ejemplo = """Este es un archivo de ejemplo.
Contiene varias líneas de texto.
Se usa para demostrar la lectura de archivos.
¡Python es genial para manejar archivos!"""
    
    escribir_archivo_texto(archivo_ejemplo, contenido_ejemplo)
    leer_archivo_texto(archivo_ejemplo)
    contar_palabras_archivo(archivo_ejemplo)
    
    print("\n" + "="*40)
    trabajar_con_json()
    
    print("\n" + "="*40)
    trabajar_con_csv()
    
    print("\n" + "="*40)
    listar_archivos_directorio()
    
    print("\n" + "="*40)
    crear_archivo_log()
    
    # Limpiar archivo de ejemplo
    if os.path.exists(archivo_ejemplo):
        os.remove(archivo_ejemplo)
        print(f"\nArchivo {archivo_ejemplo} eliminado")

if __name__ == "__main__":
    main()