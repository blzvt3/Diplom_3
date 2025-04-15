import allure
from locators import Locators
from pages.base_page import BasePage

class OrderFeedPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = Locators

    @allure.step("Подождать кликабельности кнопки «Лента Заказов»")
    def wait_clickability_of_order_feed_button(self):
        return self.wait_visibility_of_element(self.locators.ORDER_FEED_BUTTON)

    @allure.step("Кликнуть на кнопку «Лента Заказов»")
    def click_on_order_feed_button(self):
        self.click_on_element(self.locators.ORDER_FEED_BUTTON)

    @allure.step("Подождать появления заголовка «Лента заказов»")
    def wait_visibility_of_order_feed_title(self):
        return self.wait_visibility_of_element(self.locators.ORDER_FEED_TITLE)

    @allure.step("Подождать появления номера заказа из раздела «В работе»")
    def wait_visibility_of_order_number_in_work(self):
        return self.wait_visibility_of_element(self.locators.ORDER_NUMBER_IN_WORK)

    @allure.step("Получить номер заказа из раздела «В работе»")
    def get_order_number_in_work(self):
        return self.get_text_of_element(self.locators.ORDER_NUMBER_IN_WORK)

    @allure.step("Подождать кликабельности кнопки созданного заказа в ленте")
    def wait_clickability_of_order_in_feed_button(self):
        return self.wait_clickability_of_element(self.locators.ORDER_IN_FEED_BUTTON)

    @allure.step("Кликнуть на кнопку созданного заказа в ленте")
    def click_on_order_in_feed_button(self):
        self.click_on_element(self.locators.ORDER_IN_FEED_BUTTON)

    @allure.step("Подождать отображения номера заказа в деталях заказа")
    def wait_visibility_of_order_number_in_details(self):
        return self.wait_clickability_of_element(self.locators.ORDER_NUMBER_IN_DETAILS)

    @allure.step("Получить номер заказа из деталей заказа")
    def get_order_number_in_details(self):
        return self.get_text_of_element(self.locators.ORDER_NUMBER_IN_DETAILS)

    @allure.step("Подождать отображения количества заказов, выполненных за все время")
    def wait_visibility_of_completed_orders_for_all_time(self):
        return self.wait_clickability_of_element(self.locators.COMPLETED_ORDERS_ALL_TIME)

    @allure.step("Получить количество заказов, выполненных за все время")
    def get_completed_orders_for_all_time(self):
        return self.get_text_of_element(self.locators.COMPLETED_ORDERS_ALL_TIME)

    @allure.step("Подождать отображения количества заказов, выполненных за сегодня")
    def wait_visibility_of_completed_orders_for_today(self):
        return self.wait_clickability_of_element(self.locators.COMPLETED_ORDERS_TODAY)

    @allure.step("Получить количество заказов, выполненных за сегодня")
    def get_completed_orders_for_today(self):
        return self.get_text_of_element(self.locators.COMPLETED_ORDERS_TODAY)