from selenium.webdriver.common.by import By
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site/")

driver.find_element(By.XPATH, "//header/nav[1]/a[1]").click()


# Найди поле "Email" и заполни его
driver.find_element(By.XPATH, "//body/div[@id='root']/div[1]/main[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/input[1]").send_keys("alexeygvozdev31777")

# Найди поле "Пароль" и заполни его
driver.find_element(By.XPATH, "//body/div[@id='root']/div[1]/main[1]/div[1]/form[1]/fieldset[2]/div[1]/div[1]/input[1]").send_keys("some12345")


# Найди кнопку "Войти" и кликни по ней
driver.find_element(By.XPATH, "//div[@id='root']/div/main/div/form/button").click()


time.sleep(3)
driver.quit()
