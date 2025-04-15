import allure
from locators import Locators
from pages.base_page import BasePage

class PasswordRecoveryPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = Locators

    @allure.step("Подождать появления кнопки «Восстановить»")
    def wait_visibility_of_password_recovery_button(self):
        return self.wait_visibility_of_element(self.locators.PASSWORD_RECOVERY_BUTTON)

    @allure.step("Кликнуть на кнопку «Восстановить»")
    def click_on_password_recovery_button(self):
        self.click_on_element(self.locators.PASSWORD_RECOVERY_BUTTON)

    @allure.step("Заполнить поле «Email»")
    def fill_email(self, email):
        self.fill_input(self.locators.EMAIL_INPUT, email)

    @allure.step("Подождать появления поля «Пароль»")
    def wait_visibility_of_password_field(self):
        return self.wait_visibility_of_element(self.locators.PASSWORD_INPUT)

    @allure.step("Кликнуть на кнопку показать/скрыть пароль")
    def click_on_show_password_button(self):
        self.click_on_element(self.locators.SHOW_PASSWORD_BUTTON)

    @allure.step("Подождать появления подсветки поля «Пароль»")
    def wait_visibility_of_active_password_field(self):
        return self.wait_visibility_of_element(self.locators.ACTIVE_PASSWORD_FIELD)
