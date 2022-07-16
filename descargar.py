#Descargo archivos y cierro navegador
#Con errores menores pero funciona 15/07/22
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://ruta1000.com.ar/")
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
time.sleep(1)
driver.switch_to.frame(0)
driver.find_element(By.CSS_SELECTOR, "tr:nth-child(3) > td:nth-child(2) > .littlelink").click()
time.sleep(1)
driver.find_element(By.LINK_TEXT, "RESULTADOS EN EXCEL").click()
time.sleep(1)
driver.find_element(By.XPATH, "//a[contains(@href, \'timberos_top/q_nacional.xls\')]").click()
driver.find_element(By.XPATH, "//a[contains(@href, \'timberos_top/q_baires.xls\')]").click()
driver.find_element(By.XPATH, "//a[contains(@href, \'timberos_top/q_montevideo.xls\')]").click()
time.sleep(1)
driver.close()