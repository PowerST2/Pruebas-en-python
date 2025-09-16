#!/usr/bin/env python3
"""
Script principal para ejecutar todos los scripts de prueba
Menú centralizado para acceder a diferentes ejemplos y ejercicios
"""

import os
import sys
import importlib.util

def cargar_script(ruta_script):
    """Carga y ejecuta un script Python dinámicamente"""
    try:
        spec = importlib.util.spec_from_file_location("script", ruta_script)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return module
    except Exception as e:
        print(f"Error al cargar el script: {e}")
        return None

def listar_scripts_categoria(categoria):
    """Lista los scripts disponibles en una categoría"""
    ruta_categoria = os.path.join("scripts", categoria)
    if not os.path.exists(ruta_categoria):
        return []
    
    scripts = []
    for archivo in os.listdir(ruta_categoria):
        if archivo.endswith(".py"):
            scripts.append(archivo)
    return sorted(scripts)

def mostrar_menu_principal():
    """Muestra el menú principal"""
    print("\n" + "="*60)
    print("🐍 REPOSITORIO DE SCRIPTS PYTHON - MENU PRINCIPAL")
    print("="*60)
    print("📁 Categorías disponibles:")
    print("  1. Básicos - Conceptos fundamentales de Python")
    print("  2. Intermedio - Scripts más avanzados")
    print("  3. Ejemplos - Casos de uso comunes")
    print("  4. Utilidades - Herramientas útiles")
    print("  5. Explorar directorio de scripts")
    print("  6. Información del repositorio")
    print("  7. Salir")
    print("-"*60)

def mostrar_menu_categoria(categoria):
    """Muestra los scripts de una categoría específica"""
    scripts = listar_scripts_categoria(categoria)
    
    if not scripts:
        print(f"No se encontraron scripts en la categoría '{categoria}'")
        return None
    
    print(f"\n📁 Scripts en '{categoria}':")
    for i, script in enumerate(scripts, 1):
        nombre_limpio = script.replace('.py', '').replace('_', ' ').title()
        print(f"  {i}. {nombre_limpio}")
    print(f"  {len(scripts) + 1}. Volver al menú principal")
    
    return scripts

def ejecutar_script(categoria, nombre_script):
    """Ejecuta un script específico"""
    ruta_script = os.path.join("scripts", categoria, nombre_script)
    
    if not os.path.exists(ruta_script):
        print(f"Error: No se encontró el script {ruta_script}")
        return
    
    print(f"\n🚀 Ejecutando: {nombre_script}")
    print("="*50)
    
    try:
        # Cambiar al directorio del script temporalmente
        directorio_original = os.getcwd()
        os.chdir(os.path.dirname(ruta_script))
        
        # Ejecutar el script
        with open(nombre_script, 'r', encoding='utf-8') as f:
            codigo = f.read()
        
        exec(codigo)
        
        # Volver al directorio original
        os.chdir(directorio_original)
        
    except Exception as e:
        print(f"Error al ejecutar el script: {e}")
    finally:
        os.chdir(directorio_original)
    
    input("\n📍 Presiona Enter para continuar...")

def mostrar_info_repositorio():
    """Muestra información sobre el repositorio"""
    print("\n" + "="*60)
    print("📋 INFORMACIÓN DEL REPOSITORIO")
    print("="*60)
    print("📝 Propósito:")
    print("   Este repositorio contiene scripts de Python simples y básicos")
    print("   para practicar y entender diferentes conceptos de programación.")
    print()
    print("📁 Estructura:")
    print("   /scripts/")
    print("   ├── basicos/      - Conceptos fundamentales")
    print("   ├── intermedio/   - Scripts más avanzados") 
    print("   ├── ejemplos/     - Casos de uso comunes")
    print("   ├── utilidades/   - Herramientas útiles")
    print("   └── avanzado/     - Scripts complejos")
    print()
    print("🛠️  Dependencias:")
    print("   - requests")
    print("   - pandas") 
    print("   - openpyxl")
    print()
    print("💡 Uso:")
    print("   1. Ejecuta 'python run_scripts.py' para el menú principal")
    print("   2. Navega por las categorías")
    print("   3. Ejecuta scripts individuales")
    print("   4. Instala dependencias con 'pip install -r requirements.txt'")

def explorar_directorio():
    """Explora el directorio de scripts"""
    print("\n📁 Explorando directorio de scripts:")
    print("-"*40)
    
    for categoria in ["basicos", "intermedio", "ejemplos", "utilidades", "avanzado"]:
        ruta = os.path.join("scripts", categoria)
        if os.path.exists(ruta):
            scripts = listar_scripts_categoria(categoria)
            print(f"📂 {categoria}/ ({len(scripts)} scripts)")
            for script in scripts:
                print(f"   📄 {script}")
        else:
            print(f"📂 {categoria}/ (vacío)")

def main():
    """Función principal del menú"""
    while True:
        mostrar_menu_principal()
        
        try:
            opcion = input("Elige una opción (1-7): ").strip()
            
            if opcion == "1":  # Básicos
                scripts = mostrar_menu_categoria("basicos")
                if scripts:
                    sub_opcion = input(f"Elige un script (1-{len(scripts)+1}): ").strip()
                    if sub_opcion.isdigit():
                        indice = int(sub_opcion) - 1
                        if 0 <= indice < len(scripts):
                            ejecutar_script("basicos", scripts[indice])
                            
            elif opcion == "2":  # Intermedio
                scripts = mostrar_menu_categoria("intermedio")
                if scripts:
                    sub_opcion = input(f"Elige un script (1-{len(scripts)+1}): ").strip()
                    if sub_opcion.isdigit():
                        indice = int(sub_opcion) - 1
                        if 0 <= indice < len(scripts):
                            ejecutar_script("intermedio", scripts[indice])
                            
            elif opcion == "3":  # Ejemplos
                scripts = mostrar_menu_categoria("ejemplos")
                if scripts:
                    sub_opcion = input(f"Elige un script (1-{len(scripts)+1}): ").strip()
                    if sub_opcion.isdigit():
                        indice = int(sub_opcion) - 1
                        if 0 <= indice < len(scripts):
                            ejecutar_script("ejemplos", scripts[indice])
                            
            elif opcion == "4":  # Utilidades
                scripts = mostrar_menu_categoria("utilidades")
                if scripts:
                    sub_opcion = input(f"Elige un script (1-{len(scripts)+1}): ").strip()
                    if sub_opcion.isdigit():
                        indice = int(sub_opcion) - 1
                        if 0 <= indice < len(scripts):
                            ejecutar_script("utilidades", scripts[indice])
                            
            elif opcion == "5":  # Explorar
                explorar_directorio()
                input("\n📍 Presiona Enter para continuar...")
                
            elif opcion == "6":  # Info
                mostrar_info_repositorio()
                input("\n📍 Presiona Enter para continuar...")
                
            elif opcion == "7":  # Salir
                print("\n👋 ¡Gracias por usar el repositorio de scripts Python!")
                print("¡Sigue practicando y aprendiendo! 🐍")
                break
                
            else:
                print("❌ Opción no válida. Intenta de nuevo.")
                
        except KeyboardInterrupt:
            print("\n\n👋 ¡Hasta luego!")
            break
        except Exception as e:
            print(f"❌ Error inesperado: {e}")

if __name__ == "__main__":
    # Verificar que estamos en el directorio correcto
    if not os.path.exists("scripts"):
        print("❌ Error: No se encontró el directorio 'scripts'")
        print("   Asegúrate de ejecutar este script desde la raíz del repositorio")
        sys.exit(1)
    
    main()