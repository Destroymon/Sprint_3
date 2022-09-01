import locators
from locators import *
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestRegistration:
    # Регистрация на сайте
    def test_registration_in_site(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://stellarburgers.nomoreparties.site/")
        self.driver.find_element(By.XPATH, locators.Enter_LK).click()  # Нажатие на кнопку ЛК
        self.driver.find_element(By.XPATH, locators.regestration).click()  # Жмем на кнопку Войти в аккаунт
        self.driver.find_element(By.XPATH, locators.reg_mail).send_keys(email1)  # вводим емейл
        self.driver.find_element(By.XPATH, locators.reg_pass).send_keys("123456")  # вводим пароль
        self.driver.find_element(By.XPATH, locators.reg_name).send_keys("Alexey")
        self.driver.find_element(By.XPATH, locators.regestration_button).click()  # нажим на кнопку регистрации
        self.driver.find_element(By.XPATH, locators.email).send_keys(email1)  # вводим емейл
        self.driver.find_element(By.XPATH, locators.passs).send_keys("123456")  # вводим пароль
        self.driver.find_element(By.XPATH, locators.Enter).click()  # Входим под новым пользолвателем
        # проверяем результат авторизации
        self.driver.find_element(By.XPATH, locators.Enter_LK).click()
        assert self.driver.find_element(By.XPATH, locators.profile_info) # Проверяем что появились элементы пользователя которого мы создали
        assert self.driver.find_element(By.XPATH, locators.history_orders)
        assert self.driver.find_element(By.XPATH, locators.exit)
        self.driver.quit()
    # Ложный пароль
    def test_error_short_password(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://stellarburgers.nomoreparties.site/")
        self.driver.find_element(By.XPATH, locators.Enter_LK).click()  # Нажатие на кнопку ЛК
        self.driver.find_element(By.XPATH, locators.regestration).click()  # Жмем на кнопку Войти в аккаунт
        self.driver.find_element(By.XPATH, locators.reg_mail).send_keys(email1)  # вводим емейл
        self.driver.find_element(By.XPATH, locators.reg_pass).send_keys("123")  # вводим пароль
        self.driver.find_element(By.XPATH, locators.reg_name).send_keys("Alexey")
        self.driver.find_element(By.XPATH, locators.regestration_button).click()  # нажим на кнопку регистрации
        assert self.driver.find_element(By.XPATH, locators.eror) # проверяем что появмился индикатор ошибки
        self.driver.quit()
