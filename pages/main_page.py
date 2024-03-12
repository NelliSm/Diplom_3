from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from data import DataUrl
from pages.base_page import BasePage
from locators import Locators
import allure


class MainPage(BasePage):

    @allure.step('метод создания заказа авторизованным пользователем')
    def make_order(self, driver):
        order = MainPage(driver)
        order.authorization_user(driver)
        WebDriverWait(driver, 5).until(expected_conditions.url_to_be(f"{DataUrl.URL}/"))
        ingredient = driver.find_element(*Locators.INGRED_BREAD)
        add_to_order = driver.find_element(*Locators.BASKET)
        ActionChains(driver).drag_and_drop(ingredient, add_to_order).perform()
        driver.find_element(*Locators.PLACE_ORDER).click()
