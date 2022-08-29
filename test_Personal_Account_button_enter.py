from selenium.webdriver.common.by import By
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site/")

# Войти в аккаунт на главной через ЛК
driver.find_element(By.XPATH, "//p[contains(text(),'Личный Кабинет')]").click()

time.sleep(3)
driver.quit()
