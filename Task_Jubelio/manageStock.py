from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

import time

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://app.jubelio.com/login")
elem = driver.find_element(By.XPATH,"//input[@name='email']").send_keys("qa.rakamin.jubelio@gmail.com")
elem = driver.find_element(By.XPATH,"//input[@name='password']").send_keys("Jubelio123!")
elem = driver.find_element(By.XPATH,"//span[@class='ladda-label']").click()
time.sleep(3)
elem = driver.find_element(By.XPATH,"(//a[@class='metismenu-link'])[2]").click()
# time.sleep(5)
elem = driver.find_element(By.XPATH,"(//span[contains(text(),'Persediaan')])[1]").click()
time.sleep(5)
elem = driver.find_element(By.XPATH,"//button[@class='ladda-button btn btn-primary m-l-xs']").click()
time.sleep(3)
elem = driver.find_element(By.XPATH,"(//div[@class='react-grid-Cell__value'])[1]")
action = ActionChains(driver)
action.double_click(on_element=elem)
action.perform()
elem = driver.find_element(By.XPATH, "/html[1]/body[1]/div[6]/div[1]/div[1]/div[2]/div[1]/input[1]").send_keys("macbook air m1")
time.sleep(3)
action.send_keys(Keys.ENTER)
action.perform()
time.sleep(3)
elem = driver.find_element(By.XPATH, "//div[@class='react-grid-Cell']//div[@class='react-grid-Cell__value']//div//div[@class='text-right'][normalize-space()='1']")
time.sleep(3)
action.double_click(on_element=elem)
# bisa langsung dilakukan send element
action.send_keys("1")
action.send_keys(Keys.TAB)
action.perform()
time.sleep(3)
# Harga Pokok
elem = driver.find_element(By.XPATH, "//body/div[@id='root']/div[@class='content']/div[@id='wrapper']/div[@id='page-wrapper']/div[@class='wrapper wrapper-content']/div/div/div/div/div/div[@class='row']/div[@class='col-lg-12']/div[@class='page-editor']/div/div[@class='form-horizontal']/div[@class='row m-t-md']/div[@class='col-md-12']/div/div/div/div[@class='react-grid-Container']/div[@class='react-grid-Main']/div[@class='react-grid-Grid']/div/div[@class='react-grid-Viewport']/div[@class='react-grid-Canvas']/div/div/div[@class='react-grid-Row react-grid-Row--even']/div[6]/div[1]")
time.sleep(3)
action.double_click(on_element=elem)
action.send_keys("12999000 ")
action.send_keys(Keys.TAB)
action.perform()
time.sleep(3)
elem = driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[3]/div[1]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/button[1]/span[1]").click()
# Menunggu keluar
time.sleep(10)
driver.quit()
