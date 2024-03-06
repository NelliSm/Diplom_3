import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from data import DataUrl
from locators import Locators
from pages.base_page import BasePage


class TestPersonalAccount:

    @allure.title('Проверка перехода в личный кабинет')
    @allure.description('Переход по клику на «Личный кабинет». После авторизации переход в раздел «История заказов» '
                        'и выход из аккаунта')
    def test_check_personal_account_and_history_orders_and_logout(self, driver):
        user = BasePage(driver)
        driver.get(DataUrl.URL)
        driver.find_element(*Locators.BUTTON_PERSONAL_ACCOUNT).click()
        user.authorization_user(driver)
        driver.find_element(*Locators.BUTTON_PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.url_to_be(DataUrl.URL + DataUrl.PROFILE))
        driver.find_element(*Locators.ORDER_HISTORY).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.url_to_be(DataUrl.URL + DataUrl.ORDER_HISTORY))
        driver.find_element(*Locators.BUTTON_EXIT).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.url_contains(DataUrl.URL + DataUrl.LOGIN))
        assert DataUrl.LOGIN in driver.current_url
