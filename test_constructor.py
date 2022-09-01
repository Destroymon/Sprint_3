import locators
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestConstructor:
    def test_switching_between_fillers(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://stellarburgers.nomoreparties.site/")
        self.driver.find_element(By.XPATH, locators.Sous).click() # Переключаемся в раздел соусы
        assert self.driver.find_element(By.XPATH, locators.soys_3)  # смотрим что раздел с наполнетелем появился
        self.driver.find_element(By.XPATH, locators.bulka).click() # Переключаемся в раздел булки
        assert self.driver.find_element(By.XPATH, locators.bulka_inside) # смотрим что раздел с наполнителем появился
        self.driver.find_element(By.XPATH, locators.inside).click() # Переключаемся в раздел начинки
        assert self.driver.find_element(By.XPATH, locators.nachinka)  # смотрим что раздел с наполнителем появился
        self.driver.quit()
