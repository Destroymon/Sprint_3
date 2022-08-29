from selenium.webdriver.common.by import By
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site/")

# Переход к разделу Соусы
driver.find_element(By.XPATH, "//body/div[@id='root']/div[1]/main[1]/section[1]/div[1]").click()

# Переход к разделу Булки
driver.find_element(By.XPATH, "//body/div[@id='root']/div[1]/main[1]/section[1]/div[1]/div[1]").click()

# Переход к разделу Соусы
driver.find_element(By.XPATH, "//body/div[@id='root']/div[1]/main[1]/section[1]/div[1]/div[3]").click()


time.sleep(3)
driver.quit()
