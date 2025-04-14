import allure
from locators import Locators
from pages.base_page import BasePage

class AccountPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = Locators

    @allure.step("Подождать кликабельности кнопки «Личный кабинет»")
    def wait_clickability_of_account_button(self):
        return self.wait_clickability_of_element(self.locators.ACCOUNT_BUTTON)

    @allure.step("Кликнуть на кнопку «Личный кабинет»")
    def click_on_account_button(self):
        self.click_on_element(self.locators.ACCOUNT_BUTTON)

    @allure.step("Подождать кликабельности кнопки «История заказов»")
    def wait_clickability_of_order_history_button(self):
        return self.wait_clickability_of_element(self.locators.ORDER_HISTORY_BUTTON)

    @allure.step("Кликнуть на кнопку «История заказов»")
    def click_on_order_history_button(self):
        self.click_on_element(self.locators.ORDER_HISTORY_BUTTON)

    @allure.step("Подождать появления номера заказа")
    def wait_visibility_of_order_number(self):
        return self.wait_visibility_of_element(self.locators.ORDER_NUMBER_IN_HISTORY)

    @allure.step("Получить номер заказа")
    def get_order_number(self):
        return self.get_text_of_element(self.locators.ORDER_NUMBER_IN_HISTORY)

    @allure.step("Подождать кликабельности кнопки «Выход»")
    def wait_clickability_of_sign_out_button(self):
        return self.wait_clickability_of_element(self.locators.SIGN_OUT_BUTTON)

    @allure.step("Кликнуть на кнопку «Выход»")
    def click_on_sign_out_button(self):
        self.click_on_element(self.locators.SIGN_OUT_BUTTON)