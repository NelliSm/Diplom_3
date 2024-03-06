import time
import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from data import DataUrl
from locators import Locators
from pages.base_page import BasePage


class TestOrderFeed:

    @allure.title('Проверка раздела "Лента заказов"')
    @allure.description('если кликнуть на заказ, откроется всплывающее окно с деталями')
    def test_click_first_order_details_visible(self, driver):
        user_page = BasePage(driver)
        user_page.authorization_user(driver)
        driver.find_element(*Locators.BUTTON_PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.url_to_be(DataUrl.URL + DataUrl.PROFILE))
        driver.find_element(*Locators.ORDER_HISTORY).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(Locators.ORDER_FIRST_ACCOUNT))
        driver.find_element(*Locators.ORDER_FIRST_ACCOUNT).click()
        assert driver.find_element(*Locators.ORDER_STRUCTURE).text == 'Cостав'

    @allure.description('заказы пользователя из раздела «История заказов» '
                        'отображаются на странице «Лента заказов»')
    # в окне после создания заказа отображается №9999. Фактический номер заказа прогружается спустя время.
    # это баг тестового окружения, падение тестов допускается и происходит во всех браузерах.
    # чтобы обойти падение теста использовано запрещенное ожидание Timesleep.
    def test_order_in_the_list_orders(self, driver):
        counter = BasePage(driver)
        counter.make_order(driver)
        time.sleep(3)
        counter_orders = driver.find_element(*Locators.ORDER_NUMBER).text
        driver.find_element(*Locators.CLOSE).click()
        driver.get(DataUrl.URL + DataUrl.ORDER_FEED)
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(Locators.ORDER_FEED_ALL))
        order_feed = driver.find_element(*Locators.ORDER_FEED_ALL).text
        driver.get(DataUrl.URL + DataUrl.ORDER_HISTORY)
        counter.scroll_to_end_of_page()
        assert counter_orders in order_feed

    @allure.description('при создании нового заказа счётчик Выполнено за всё время увеличивается')
    def test_order_all_numbers_higher(self, driver):
        counter = BasePage(driver)
        driver.get(DataUrl.URL + DataUrl.ORDER_FEED)
        current_counter_orders = driver.find_element(*Locators.COUNT_ORDERS).text
        counter.make_order(driver)
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.ORDER_NUMBER))
        driver.find_element(*Locators.CLOSE).click()
        driver.get(DataUrl.URL + DataUrl.ORDER_FEED)
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.COUNT_ORDERS))
        new_current_counter_orders = driver.find_element(*Locators.COUNT_ORDERS).text
        assert int(new_current_counter_orders) == int(current_counter_orders) + 1

    @allure.description('при создании нового заказа счётчик Выполнено за сегодня увеличивается')
    def test_order_all_numbers_today_higher(self, driver):
        counter = BasePage(driver)
        driver.get(DataUrl.URL + DataUrl.ORDER_FEED)
        current_counter_orders_today = driver.find_element(*Locators.COUNT_ORDERS_TODAY).text
        counter.make_order(driver)
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.ORDER_NUMBER))
        driver.find_element(*Locators.CLOSE).click()
        driver.get(DataUrl.URL + DataUrl.ORDER_FEED)
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.COUNT_ORDERS_TODAY))
        new_current_counter_orders_today = driver.find_element(*Locators.COUNT_ORDERS_TODAY).text
        assert int(new_current_counter_orders_today) == int(current_counter_orders_today) + 1

    @allure.description('после оформления заказа его номер появляется в разделе В работе')
    # в окне после создания заказа отображается №9999.
    # Фактический номер заказа прогружается спустя время.
    # это баг тестового окружения, падение тестов допускается и происходит во всех браузерах.
    # чтобы обойти падение теста использовано запрещенное ожидание Timesleep.
    def test_order_number_at_work(self, driver):
        counter = BasePage(driver)
        driver.get(DataUrl.URL + DataUrl.ORDER_FEED)
        counter_orders = driver.find_element(*Locators.COUNT_ORDERS).text
        counter.make_order(driver)
        time.sleep(3)
        driver.find_element(*Locators.CLOSE).click()
        driver.get(DataUrl.URL + DataUrl.ORDER_FEED)
        time.sleep(3)
        order_at_work = driver.find_element(*Locators.ORDER_AT_WORK).text
        assert int(counter_orders) == int(order_at_work)
