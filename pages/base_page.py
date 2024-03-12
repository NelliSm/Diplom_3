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

    @allure.step('Скролл страницы до элемента')
    def scroll_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Скролл  страницы до конца страницы')
    def scroll_to_end_of_page(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
