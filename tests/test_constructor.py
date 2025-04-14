import allure
from pages.account_page import AccountPage
from pages.constructor_page import ConstructorPage
from pages.order_feed_page import OrderFeedPage

class TestConstructor:
    @allure.title('Проверка перехода в раздел «Конструктор» и отображения деталей ингредиента')
    def test_ingredient_details(self, driver_unauthorized_user):
        constructor_page = ConstructorPage(driver_unauthorized_user)
        constructor_page.wait_invisibility_of_overlay()

        order_feed_page = OrderFeedPage(driver_unauthorized_user)
        order_feed_page.wait_clickability_of_order_feed_button()
        order_feed_page.click_on_order_feed_button()
        order_feed_page.wait_visibility_of_order_feed_title()

        constructor_page.wait_clickability_of_constructor_button()
        constructor_page.click_on_constructor_button()
        constructor_page.wait_clickability_of_r2_d3_bun_button()
        constructor_page.click_on_r2_d3_bun_button()
        assert constructor_page.wait_visibility_of_ingredient_details_title()
        constructor_page.click_on_ingredient_details_close_button()
        assert constructor_page.wait_invisibility_of_ingredient_details_title()

    @allure.title('Проверка каунтера ингредиента')
    def test_ingredient_counter(self, driver_unauthorized_user):
        constructor_page = ConstructorPage(driver_unauthorized_user)
        constructor_page.wait_invisibility_of_overlay()
        constructor_page.wait_clickability_of_r2_d3_bun_button()
        constructor_page.move_r2_d3_bun_to_basket()
        constructor_page.wait_visibility_of_r2_d3_bun_top_in_basket()
        constructor_page.wait_visibility_of_r2_d3_bun_bottom_in_basket()
        assert constructor_page.get_text_of_r2_d3_bun_counter() == "2"

    @allure.title('Проверка создания заказа')
    def test_create_order(self, driver_authorized_user):
        constructor_page = ConstructorPage(driver_authorized_user)
        constructor_page.wait_invisibility_of_overlay()
        constructor_page.wait_clickability_of_r2_d3_bun_button()
        constructor_page.move_r2_d3_bun_to_basket()
        constructor_page.wait_visibility_of_r2_d3_bun_top_in_basket()
        constructor_page.wait_visibility_of_r2_d3_bun_bottom_in_basket()
        constructor_page.click_on_order_button()
        constructor_page.wait_invisibility_of_overlay()
        constructor_page.wait_visibility_of_order_number()
        assert constructor_page.get_order_number().isdigit()
