from selenium.webdriver.common.by import By
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site/")

# Войти в аккаунт на главной
driver.find_element(By.XPATH, "//button[contains(text(),'Войти в аккаунт')]").click()

time.sleep(3)
driver.quit()
