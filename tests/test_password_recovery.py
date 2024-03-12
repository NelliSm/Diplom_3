import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators
from data import DataUrl


@allure.suite('Восстановление пароля')
class TestPasswordRecover:

    @allure.title('Тест восстановления пароля')
    @allure.description('Переход на страницу восстановления пароля по кнопке «Восстановить пароль», ввод почты и клик '
                        'по кнопке Восстановить. Клик по кнопке показать/скрыть пароль делает поле активным -'
                        'подсвечивает его.')
    def test_button_recovery_form(self, driver):
        driver.get(DataUrl.URL + DataUrl.LOGIN)
        driver.find_element(*Locators.BUT_RECOVER).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.url_to_be(DataUrl.URL + DataUrl.RECOVER))
        driver.find_element(*Locators.BUTTON_RECOVER_PASSWORD).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.url_to_be(DataUrl.URL + DataUrl.RESET))
        active_field = "input__placeholder-focused"
        driver.find_element(*Locators.EYE_BUTTON).click()
        password_field = driver.find_element(*Locators.BEFORE_CLICK)
        assert active_field in password_field.get_attribute("class")
