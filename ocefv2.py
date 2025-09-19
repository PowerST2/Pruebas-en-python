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

def main():
    url = 'https://inscripcion.admision.uni.edu.pe'
    carpeta = r'C:\temp'
    archivos_en_carpeta = os.listdir(carpeta)
    archivos_xls = [archivo for archivo in archivos_en_carpeta if archivo.lower().endswith('.xls')]

    for archivo_xls in archivos_xls:
        ruta_completa = os.path.join(carpeta, archivo_xls)
        try:
            os.remove(ruta_completa)
            print(f"Eliminado: {ruta_completa}")
        except Exception as e:
            print(f"No se pudo eliminar {ruta_completa}. Error: {e}")
    download_folder = "C:\\Temp"
    options = Options()
    options.add_experimental_option("prefs", {
        "download.default_directory": download_folder,
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing.enabled": False,  # Desactiva la navegación segura
        "safebrowsing.disable_download_protection": True,  # Desactiva la protección de descargas
        "profile.default_content_settings.popups": 0,
        "profile.default_content_setting_values.automatic_downloads": 1,  # Permite descargas automáticas
        "profile.content_settings.exceptions.automatic_downloads.*.setting": 1,
        # Permitir descargas automáticas para todos los sitios
        "profile.default_content_setting_values.mixed_script": 1,  # Permitir contenido mixto (HTTP y HTTPS)
        "profile.default_content_setting_values.ssl_cert_decisions": 1  # Permitir certificados SSL
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
    driver.get(url + '/admin/pagos')
    botonsct = driver.find_element(By.ID, 'crear_cartera_nueva')
    botonsct.click()
    time.sleep(10)


    ruta_excel = "C:\\temp\\reporteocef.xls"

# Iniciar Excel
    excel = win32com.client.Dispatch("Excel.Application")

# Hacer Excel visible (opcional)
    excel.Visible = True

# Abrir el archivo
    print(f'abrir excel')
    workbook = excel.Workbooks.Open(ruta_excel)

    workbook.Save()

# Aquí podrías realizar más operaciones con el archivo
    time.sleep(10)
# Cerrar el libro sin guardar cambios
    workbook.Close(False)

# Cerrar Excel
    excel.Quit()


if __name__ == "__main__":
    main()