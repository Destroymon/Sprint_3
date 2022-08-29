from selenium.webdriver.common.by import By
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site/")

# Войти в аккаунт на главной
driver.find_element(By.XPATH, "//button[contains(text(),'Войти в аккаунт')]").click()

# Найди кнопку "Войти" и кликни по ней
driver.find_element(By.XPATH, "//div[@id='root']/div/main/div/form/button").click()

# Перейти в форму восстановления пароля
driver.find_element(By.XPATH, "//a[contains(text(),'Восстановить пароль')]").click()

time.sleep(1)

# Нажать на кнопку войти в форме регестрации
driver.find_element(By.XPATH, "//a[contains(text(),'Войти')]").click()

time.sleep(3)
driver.quit()
