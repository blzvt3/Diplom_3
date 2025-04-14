import allure
from pages.constructor_page import ConstructorPage
from pages.order_feed_page import OrderFeedPage

class TestOrderFeed:
    @allure.title('Проверка отображения номера заказа в разделе «В работе»')
    def test_order_number_in_work(self, driver_authorized_user, create_order):
        order_number = create_order
        constructor_page = ConstructorPage(driver_authorized_user)
        constructor_page.wait_invisibility_of_overlay()

        order_feed_page = OrderFeedPage(driver_authorized_user)
        order_feed_page.wait_clickability_of_order_feed_button()
        order_feed_page.click_on_order_feed_button()
        order_feed_page.wait_visibility_of_order_number_in_work()
        assert order_number in order_feed_page.get_order_number_in_work()

    @allure.title('Проверка отображения деталей заказа')
    def test_order_details(self, driver_authorized_user, create_order):
        order_number = create_order
        constructor_page = ConstructorPage(driver_authorized_user)
        constructor_page.wait_invisibility_of_overlay()

        order_feed_page = OrderFeedPage(driver_authorized_user)
        order_feed_page.wait_clickability_of_order_feed_button()
        order_feed_page.click_on_order_feed_button()
        order_feed_page.wait_clickability_of_order_in_feed_button()
        order_feed_page.click_on_order_in_feed_button()
        order_feed_page.wait_visibility_of_order_number_in_details()
        assert order_number in order_feed_page.get_order_number_in_details()

    @allure.title('Проверка изменения количества заказов, выполненных за все время')
    def test_completed_orders_for_all_time(self, driver_authorized_user, request):
        constructor_page = ConstructorPage(driver_authorized_user)
        constructor_page.wait_invisibility_of_overlay()

        order_feed_page = OrderFeedPage(driver_authorized_user)
        order_feed_page.wait_clickability_of_order_feed_button()
        order_feed_page.click_on_order_feed_button()
        order_feed_page.wait_visibility_of_completed_orders_for_all_time()

        completed_orders_before = int(order_feed_page.get_completed_orders_for_all_time())
        request.getfixturevalue("create_order")
        completed_orders_after = int(order_feed_page.get_completed_orders_for_all_time())
        assert completed_orders_after == completed_orders_before + 1

    @allure.title('Проверка изменения количества заказов, выполненных за сегодня')
    def test_completed_orders_for_today(self, driver_authorized_user, request):
        constructor_page = ConstructorPage(driver_authorized_user)
        constructor_page.wait_invisibility_of_overlay()

        order_feed_page = OrderFeedPage(driver_authorized_user)
        order_feed_page.wait_clickability_of_order_feed_button()
        order_feed_page.click_on_order_feed_button()
        order_feed_page.wait_visibility_of_completed_orders_for_today()

        completed_orders_before = int(order_feed_page.get_completed_orders_for_today())
        request.getfixturevalue("create_order")
        completed_orders_after = int(order_feed_page.get_completed_orders_for_today())
        assert completed_orders_after == completed_orders_before + 1