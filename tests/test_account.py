import allure
from pages.account_page import AccountPage
from pages.constructor_page import ConstructorPage
from pages.login_page import LoginPage

class TestAccount:
    @allure.title('Проверка отображения истории заказов в личном кабинете')
    def test_order_history(self, driver_authorized_user, create_order):
        order_number = create_order
        constructor_page = ConstructorPage(driver_authorized_user)
        constructor_page.wait_invisibility_of_overlay()

        account_page = AccountPage(driver_authorized_user)
        account_page.wait_clickability_of_account_button()
        account_page.click_on_account_button()
        account_page.wait_clickability_of_order_history_button()
        account_page.click_on_order_history_button()
        account_page.wait_visibility_of_order_number()
        assert order_number in account_page.get_order_number()

    @allure.title('Проверка выхода из аккаунта')
    def test_sign_out(self, driver_authorized_user):
        constructor_page = ConstructorPage(driver_authorized_user)
        constructor_page.wait_invisibility_of_overlay()

        account_page = AccountPage(driver_authorized_user)
        account_page.wait_clickability_of_account_button()
        account_page.click_on_account_button()
        account_page.wait_clickability_of_sign_out_button()
        account_page.click_on_sign_out_button()

        login_page = LoginPage(driver_authorized_user)
        assert login_page.wait_visibility_of_password_recovery_hyperlink()