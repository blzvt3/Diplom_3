import allure
from locators import Locators
from pages.base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = Locators

    @allure.step("Подождать появления гиперссылки «Восстановить пароль»")
    def wait_visibility_of_password_recovery_hyperlink(self):
        return self.wait_visibility_of_element(self.locators.PASSWORD_RECOVERY_HYPERLINK)

    @allure.step("Кликнуть на гиперссылку «Восстановить пароль»")
    def click_on_password_recovery_hyperlink(self):
        self.click_on_element(self.locators.PASSWORD_RECOVERY_HYPERLINK)
