from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
# inport jeda waktu
import time

driver = webdriver.Chrome()
driver.maximize_window()
# menambahkan alamat url
driver.get("https://app.jubelio.com/login")
elem = driver.find_element(By.XPATH,"//input[@name='email']").send_keys("qa.rakamin.jubelio@gmail.com")
elem = driver.find_element(By.XPATH,"//input[@name='password']").send_keys("Jubelio123!")
elem = driver.find_element(By.XPATH,"//span[@class='ladda-label']").click()

time.sleep(10)
