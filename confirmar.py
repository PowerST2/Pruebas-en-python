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
    url = 'https://simulacro.admision.uni.edu.pe'
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
    botonsct = driver.find_element(By.ID, 'confirmar_cartera')
    botonsct.click()
    time.sleep(10)


if __name__ == "__main__":
    main()