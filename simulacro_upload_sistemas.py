from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
def main():
    archivo_a_cargar = 'C:\\temp\\datos_bcp.csv'
    archivo_a_cargar_sctb = 'C:\\temp\\datos_scotiabank.csv'
    url = 'http://simulacro.admision.uni.edu.pe'
    driver = webdriver.Chrome()
    driver.get(url)
    username_field = driver.find_element(By.NAME, "dni")
    password_field = driver.find_element(By.NAME, "password")
    username_field.send_keys("jcampos")
    password_field.send_keys("niefyop2Swyt")
    password_field.send_keys(Keys.RETURN)
    time.sleep(5)
    driver.get(url+'/admin/pagos')

    time.sleep(5)
    input_archivo = driver.find_element(By.NAME, 'file')  # Cambia 'file' al atributo correcto de tu página
    input_archivo.send_keys(archivo_a_cargar)
    boton = driver.find_element(By.ID,'btnchang')
    boton.click()

   # time.sleep(20)
   # driver.get(url+'/admin/pagos')
   # input_archivo_dos = driver.find_element(By.NAME, 'file')  # Cambia 'file' al atributo correcto de tu página
   # input_archivo_dos.send_keys(archivo_a_cargar_sctb)
   # botonsct = driver.find_element(By.ID,'btnchang')
   # botonsct.click()

    driver.implicitly_wait(10)
    time.sleep(20)
    driver.quit()
if __name__ == "__main__":
    main()