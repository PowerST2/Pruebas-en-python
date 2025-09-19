from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from datetime import datetime
import time
import os


def eliminar_temporal():
    # ELIMINAR TODOS LOS ARCHIVOS .xls
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

    # Configurar el navegador


def decargar_reporte_bcp():
    download_folder = "C:\\Temp"
    options = Options()
    options.add_experimental_option("prefs", {
        "download.default_directory": download_folder,
        "download.prompt_for_download": False,  # Para evitar que se pregunte
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True
    })

    # Inicia el navegador con las opciones configuradas
    driver = webdriver.Chrome(options=options)
    driver.get("https://www.ocef.uni.edu.pe")
    username_field = driver.find_element(By.NAME, "txtUsuario")
    password_field = driver.find_element(By.NAME, "txtContraseña")
    username_field.send_keys("ocad091")
    password_field.send_keys("pagos424dos")
    password_field.send_keys(Keys.RETURN)
    driver.implicitly_wait(10)
    time.sleep(2)
    driver.get("https://www.ocef.uni.edu.pe/recaudacion/orden-pago-banco/wfrmOrdenPagoSCTB_importar.aspx")
    time.sleep(2)
    boton_Reporte = driver.find_element(By.NAME, "ctl00$cphContenido$ibReporte")
    boton_Reporte.click()
    time.sleep(2)
    fecha_inicial = driver.find_element(By.NAME, "ctl00$cphContenido$txtFechaInicial")
    fecha_inicial.click()
    time.sleep(2)
    driver.execute_script("arguments[0].setAttribute('class','vote-link up voted')", fecha_inicial)
    fecha_inicial.send_keys(Keys.CONTROL, "a")
    fecha_inicial.send_keys(Keys.BACKSPACE)
    fecha_inicial.send_keys("01/07/2025")
    comboselect = Select(driver.find_element(By.NAME, "ctl00$cphContenido$ddlEstadoVentaReporte"))
    comboselect.select_by_visible_text('Canceladas')
    time.sleep(10)
    btn_buscar = driver.find_element(By.NAME, "ctl00$cphContenido$btnBuscar_vReporte")
    btn_buscar.click()
    time.sleep(10)
    btn_export = driver.find_element(By.NAME, "ctl00$cphContenido$btnExportarExcel")
    btn_export.click()
    time.sleep(10)
    driver.quit()


def main():
    eliminar_temporal()
    decargar_reporte_bcp()


if __name__ == "__main__":
    main()