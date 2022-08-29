from selenium.webdriver.common.by import By
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site/")

# Войти в ЛК на главной
driver.find_element(By.XPATH, "//header/nav[1]/a[1]").click()


time.sleep(3)
driver.quit()
