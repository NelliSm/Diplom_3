import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from data import DataUrl
from pages.base_page import BasePage
from locators import Locators


@allure.suite('Проверка основного функционала')
class TestBasicFunctionality:

    @allure.title('Оформление заказа')
    @allure.description('Залогиненный пользователь может оформить заказ. Проверка, что после оформления заказа '
                        'отображается его номер')
    def test_user_make_order(self, driver):
        creator_order = BasePage(driver)
        creator_order.authorization_user(driver)
        WebDriverWait(driver, 5).until(
            expected_conditions.url_to_be(f"{DataUrl.URL}/"))
        ingredient = driver.find_element(*Locators.INGRED_BREAD)
        add_to_order = driver.find_element(*Locators.BASKET)
        ActionChains(driver).drag_and_drop(ingredient, add_to_order).perform()
        driver.find_element(*Locators.PLACE_ORDER).click()
        assert driver.find_element(*Locators.ORDER)

    @allure.title('Клик на "Конструктор"')
    @allure.description('Переход по клику на «Конструктор». Проверка, что текущий url соответствует ожидаемому')
    def test_click_the_constructor(self, driver):
        driver.get(DataUrl.URL + DataUrl.LOGIN)
        driver.find_element(*Locators.BUTTON_CONSTRUCTOR).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.url_contains(DataUrl.URL))
        assert DataUrl.URL in driver.current_url

    @allure.title('Клик на "Лента заказов"')
    @allure.description('Переход по клику на «Лента заказов». Проверка, что текущий url соответствует ожидаемому')
    def test_click_the_order_feed(self, driver):
        driver.get(DataUrl.URL + DataUrl.LOGIN)
        driver.find_element(*Locators.ORDER_FEED).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.url_contains(DataUrl.URL + DataUrl.ORDER_FEED))
        assert driver.current_url == DataUrl.URL + DataUrl.ORDER_FEED

    @allure.title('Клик на ингредиент')
    @allure.description('Если кликнуть на ингредиент, появится всплывающее окно с элементом "Детали ингредиента"')
    def test_click_the_ingredients(self, driver):
        driver.get(DataUrl.URL)
        driver.find_element(*Locators.INGRED_BREAD).click()
        assert driver.find_element(*Locators.DETAILS_INGRED).text == "Детали ингредиента"

    @allure.title('Окно с деталями ингредиента закрывается')
    @allure.description('Если кликнуть на ингредиент, появится всплывающее окно с деталями. '
                        'Всплывающее окно закрывается кликом по крестику')
    def test_window_with_ingredient_is_closing(self, driver):
        driver.get(DataUrl.URL)
        driver.find_element(*Locators.INGRED_BREAD).click()
        driver.find_element(*Locators.BUTTON_CLOSE_INGRED).click()
        assert len(driver.find_elements(*Locators.Wind_Close)) > 0, f"The modal window has closed"

    @allure.title('Работа счетчика добавленного в заказ ингредиента')
    @allure.description('При добавлении ингредиента в заказ счётчик этого ингридиента увеличивается')
    def test_check_quantity_after_adding_ingredient(self, driver):
        driver.get(DataUrl.URL)
        ingredient = driver.find_element(*Locators.INGRED_BREAD)
        add_to_order = driver.find_element(*Locators.BASKET)
        ActionChains(driver).drag_and_drop(ingredient, add_to_order).perform()
        count = driver.find_element(*Locators.COUNT_INGRED_BREAD).text
        assert int(count) == 2
