from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
import time
import os
def main():
        download_folder = "C:\\temp\\"
        archivo_a_cargar = "C:\\temp\\reporteocef.xls"

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
        time.sleep(2)
        username_field = driver.find_element(By.NAME, "txtUsuario")
        password_field = driver.find_element(By.NAME, "txtContraseña")
        username_field.send_keys("ocad091")
        password_field.send_keys("pagos424dos")
        password_field.send_keys(Keys.RETURN)
        driver.implicitly_wait(10)
        driver.get("https://www.ocef.uni.edu.pe/recaudacion/orden-pago-banco/wfrmOrdenPagoBCP_importar.aspx")
        time.sleep(2)
        #btn_buscar = driver.find_element(By.NAME, "ctl00$cphContenido$ibModificar")
        #btn_buscar.click()

        #time.sleep(5)
        #fecha_inicial = driver.find_element(By.NAME, "ctl00$cphContenido$txtModFechaIni")
        #fecha_inicial.click()
        #driver.execute_script("arguments[0].setAttribute('class','vote-link up voted')", fecha_inicial)
        #fecha_inicial.send_keys(Keys.CONTROL, "a")
        #fecha_inicial.send_keys(Keys.BACKSPACE)
        #fecha_inicial.send_keys("01/06/2024")
        #comboselect = Select(driver.find_element(By.NAME, "ctl00$cphContenido$ddlEstadoVentaModificar"))
        #comboselect.select_by_visible_text('Pendientes')
        #time.sleep(2)
        #btn_buscar = driver.find_element(By.NAME, "ctl00$cphContenido$btnBuscar_vModificar")
        #btn_buscar.click()
        #time.sleep(5)
        #btn_buscar = driver.find_element(By.NAME, "ctl00$cphContenido$btnEliminarMasivo")
        #btn_buscar.click()
        #time.sleep(2)
        #try:
        #        alert = driver.switch_to.alert
        #        alert.accept()
        #        time.sleep(3)
        #        alert2 = driver.switch_to.alert
        #        alert2.accept()
        #        time.sleep(3)
        #except NoAlertPresentException:
        #    print("No se encontró ningún alerta")

        btn_ingreso = driver.find_element(By.NAME, "ctl00$cphContenido$ibIngreso")
        btn_ingreso.click()
        time.sleep(3)
        espera = WebDriverWait(driver, 90)
        input_archivo = driver.find_element(By.NAME, 'ctl00$cphContenido$AsyncFileUpload1$ctl02')
        time.sleep(5)
        WebDriverWait(driver, 90)
        input_archivo.send_keys(archivo_a_cargar)
        WebDriverWait(driver, 90)
        time.sleep(15)
        try:
                alert = driver.switch_to.alert
                alert.accept()
        except NoAlertPresentException:
            print("No se encontró ningún alerta")


if __name__ == "__main__":
    main()