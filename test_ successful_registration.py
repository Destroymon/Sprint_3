from selenium.webdriver.common.by import By
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site/")

# Нажать на кнопку личный кабинет
driver.find_element(By.XPATH, "//header/nav[1]/a[1]").click()
time.sleep(3)

# Нажать на кнопку регестрации
driver.find_element(By.XPATH, "//div[@id='root']/div/main/div/div/p/a").click()
time.sleep(2)

# Найди поле "Email" и заполни его
driver.find_element(By.XPATH, "//body/div[@id='root']/div[1]/main[1]/div[1]/form[1]/fieldset[2]/div[1]/div[1]/input[1]").send_keys("alexeygvozdev31777@yandex.ru")
time.sleep(1)
# Найди поле "Пароль" и заполни его
driver.find_element(By.XPATH, "//body/div[@id='root']/div[1]/main[1]/div[1]/form[1]/fieldset[3]/div[1]/div[1]/input[1]").send_keys("123456")
time.sleep(1)
# Найти поле имя и заполнить его
driver.find_element(By.XPATH, "//body/div[@id='root']/div[1]/main[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/input[1]").send_keys("Алексей")
time.sleep(1)
# Найди кнопку Зарегестрироваться и кликни по ней
driver.find_element(By.XPATH, "//body/div[@id='root']/div[1]/main[1]").click()
time.sleep(1)
driver.quit()

