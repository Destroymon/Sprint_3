from selenium.webdriver.common.by import By
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site/")

# Войти в аккаунт на главной
driver.find_element(By.XPATH, "//header/nav[1]/a[1]").click()


# Найди поле "Email" и заполни его
driver.find_element(By.XPATH, "//body/div[@id='root']/div[1]/main[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/input[1]").send_keys("alexeygvozdev31777@yandex.ru")

# Найди поле "Пароль" и заполни его
driver.find_element(By.XPATH, "//body/div[@id='root']/div[1]/main[1]/div[1]/form[1]/fieldset[2]/div[1]/div[1]/input[1]").send_keys("123456")


# Найди кнопку "Войти" и кликни по ней
driver.find_element(By.XPATH, "//div[@id='root']/div/main/div/form/button").click()

time.sleep(1)

# Найти кнопку и перейти в ЛК
driver.find_element(By.XPATH, "//div[@id='root']/div/header/nav/a/p").click()

time.sleep(3)

# Выход из аккаунта
driver.find_element(By.XPATH, "//div[@id='root']/div/main/div/nav/ul/li[3]/button").click()

# (Без команды таймера страница не успевает загрузиться и команды не работают)
time.sleep(3)
driver.quit()
