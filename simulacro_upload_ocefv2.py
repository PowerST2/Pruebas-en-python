from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import os
import xlwt
import xlrd
from xlutils.copy import copy
import win32com.client
import pyautogui
import pygetwindow as gw

def main():
    # --- Start of simulacro_upload_sistemas.py logic ---
    archivo_a_cargar = 'C:\\temp\\datos_bcp.csv'
    archivo_a_cargar_sctb = 'C:\\temp\\datos_scotiabank.csv'
    url = 'http://simulacro.admision.uni.edu.pe'
    
    # Use options from simulacro_ocefv2.py to handle downloads
    download_folder = "C:\\Temp"
    options = Options()
    options.add_experimental_option("prefs", {
        "download.default_directory": download_folder,
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing.enabled": False,
        "safebrowsing.disable_download_protection": True,
        "profile.default_content_settings.popups": 0,
        "profile.default_content_setting_values.automatic_downloads": 1,
        "profile.content_settings.exceptions.automatic_downloads.*.setting": 1,
        "profile.default_content_setting_values.mixed_script": 1,
        "profile.default_content_setting_values.ssl_cert_decisions": 1
    })

    # Inicia el navegador con las opciones configuradas
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    username_field = driver.find_element(By.NAME, "dni")
    password_field = driver.find_element(By.NAME, "password")
    username_field.send_keys("jcampos")
    password_field.send_keys("niefyop2Swyt")
    password_field.send_keys(Keys.RETURN)
    time.sleep(5)
    driver.get(url+'/admin/pagos')

    time.sleep(5)
    input_archivo = driver.find_element(By.NAME, 'file')
    input_archivo.send_keys(archivo_a_cargar)
    boton = driver.find_element(By.ID,'btnchang')
    boton.click()

    time.sleep(5)

    driver.implicitly_wait(10)
    # --- End of simulacro_upload_sistemas.py logic (except driver.quit()) ---

    # --- Start of simulacro_ocefv2.py logic ---
    # The browser is already open and logged in.
    
    carpeta = r'C:\\temp'
    archivos_en_carpeta = os.listdir(carpeta)
    archivos_xls = [archivo for archivo in archivos_en_carpeta if archivo.lower().endswith('.xls')]

    for archivo_xls in archivos_xls:
        ruta_completa = os.path.join(carpeta, archivo_xls)
        try:
            os.remove(ruta_completa)
            print(f"Eliminado: {ruta_completa}")
        except Exception as e:
            print(f"No se pudo eliminar {ruta_completa}. Error: {e}")

    driver.get(url + '/admin/pagos')
    botonsct = driver.find_element(By.ID, 'crear_cartera_nueva')
    botonsct.click()
    time.sleep(10)

    ruta_excel = "C:\\temp\\reporteocef.xls"

    # Iniciar Excel
    excel = win32com.client.Dispatch("Excel.Application")
    excel.Visible = True

    # Abrir el archivo
    print(f'abrir excel')
    workbook = excel.Workbooks.Open(ruta_excel)

    # Seleccionar la hoja activa
    worksheet = workbook.ActiveSheet
    
    # Encontrar la última fila con datos en la columna K
    last_row = worksheet.Cells(worksheet.Rows.Count, "K").End(-4162).Row  # -4162 es xlUp
    
    # Verificar si hay datos para formatear
    if last_row >= 2:
        # Seleccionar el rango de la columna K desde la fila 2 hasta la última fila
        range_to_format = worksheet.Range(f"K2:K{last_row}")
        
        # Establecer el formato de número
        range_to_format.NumberFormat = "0"

    time.sleep(5)
    excel_window = None
    for _ in range(10):
        possible_windows = [win for win in gw.getWindowsWithTitle('Excel') if 'reporteocef' in win.title]
        if possible_windows:
            excel_window = possible_windows[0]
            break
        time.sleep(1)

    if excel_window:
        excel_window.maximize() # Maximize the window to ensure it's in the foreground
        time.sleep(1)
        excel_window.activate()
        time.sleep(3)
        pyautogui.hotkey("ctrl", "g")
        time.sleep(2)
        pyautogui.hotkey("alt", "f4")
        time.sleep(4)
    else:
        print("No se pudo encontrar la ventana de Excel con el título 'reporteocef'.")
    
    try:
        workbook.Close(SaveChanges=True)
        excel.Quit()
    except Exception as e:
        print(f"Ocurrió un error al cerrar Excel: {e}")

    # --- End of simulacro_ocefv2.py logic ---

    # Finally, close the browser
    time.sleep(5) # A small wait before closing
    driver.quit()

if __name__ == "__main__":
    main()
