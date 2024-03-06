from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from data import DataUrl, DataUser
from locators import Locators
import allure


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('метод авторизации пользователя')
    def authorization_user(self, driver):
        driver.get(DataUrl.URL + DataUrl.LOGIN)
        driver.find_element(*Locators.EMAIL_AUTHORISATION).send_keys(DataUser.LOGIN_EMAIL)
        driver.find_element(*Locators.PASSWORD_AUTHORISATION).send_keys(DataUser.LOGIN_PASSWORD)
        driver.find_element(*Locators.BUTTON_ENTER).click()

    @allure.step('метод создания заказа авторизованным пользователем')
    def make_order(self, driver):
        order = BasePage(driver)
        order.authorization_user(driver)
        WebDriverWait(driver, 5).until(expected_conditions.url_to_be(f"{DataUrl.URL}/"))
        ingredient = driver.find_element(*Locators.INGRED_BREAD)
        add_to_order = driver.find_element(*Locators.BASKET)
        ActionChains(driver).drag_and_drop(ingredient, add_to_order).perform()
        driver.find_element(*Locators.PLACE_ORDER).click()

    @allure.step('Скролл страницы до элемента')
    def scroll_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Скролл  страницы до конца страницы')
    def scroll_to_end_of_page(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
