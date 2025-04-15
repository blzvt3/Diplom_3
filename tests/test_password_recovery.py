import allure
from data import Data
from pages.constructor_page import ConstructorPage
from pages.login_page import LoginPage
from pages.account_page import AccountPage
from pages.password_recovery_page import PasswordRecoveryPage

class TestPasswordRecovery:
    @allure.title('Проверка страницы восстановления пароля')
    def test_password_recovery(self, driver_unauthorized_user):
        constructor_page = ConstructorPage(driver_unauthorized_user)
        constructor_page.wait_invisibility_of_overlay()

        account_page = AccountPage(driver_unauthorized_user)
        account_page.wait_clickability_of_account_button()
        account_page.click_on_account_button()

        login_page = LoginPage(driver_unauthorized_user)
        login_page.wait_visibility_of_password_recovery_hyperlink()
        login_page.click_on_password_recovery_hyperlink()

        password_recovery_page = PasswordRecoveryPage(driver_unauthorized_user)
        password_recovery_page.wait_visibility_of_password_recovery_button()
        password_recovery_page.fill_email(Data.email)
        password_recovery_page.click_on_password_recovery_button()
        password_recovery_page.wait_visibility_of_password_field()
        password_recovery_page.click_on_show_password_button()
        assert password_recovery_page.wait_visibility_of_active_password_field()
