import allure
from locators import Locators
from pages.base_page import BasePage

class ConstructorPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = Locators

    @allure.step("Подождать кликабельности кнопки «Конструктор»")
    def wait_clickability_of_constructor_button(self):
        return self.wait_clickability_of_element(self.locators.CONSTRUCTOR_BUTTON)

    @allure.step("Кликнуть на кнопку «Конструктор»")
    def click_on_constructor_button(self):
        self.click_on_element(self.locators.CONSTRUCTOR_BUTTON)

    @allure.step("Подождать кликабельности кнопки «Оформить заказ»")
    def wait_clickability_of_order_button(self):
        return self.wait_clickability_of_element(self.locators.ORDER_BUTTON)

    @allure.step("Кликнуть на кнопку «Оформить заказ»")
    def click_on_order_button(self):
        self.click_on_element(self.locators.ORDER_BUTTON)

    @allure.step("Подождать кликабельности кнопки «Флюоресцентная булка R2-D3»")
    def wait_clickability_of_r2_d3_bun_button(self):
        return self.wait_clickability_of_element(self.locators.R2_D3_BUN_BUTTON)

    @allure.step("Кликнуть на кнопку «Флюоресцентная булка R2-D3»")
    def click_on_r2_d3_bun_button(self):
        self.click_on_element(self.locators.R2_D3_BUN_BUTTON)

    @allure.step("Подождать появления заголовка «Детали ингредиента»")
    def wait_visibility_of_ingredient_details_title(self):
        return self.wait_visibility_of_element(self.locators.INGREDIENT_DETAILS_TITLE)

    @allure.step("Подождать исчезновения заголовка «Детали ингредиента»")
    def wait_invisibility_of_ingredient_details_title(self):
        return self.wait_invisibility_of_element(self.locators.INGREDIENT_DETAILS_TITLE)

    @allure.step("Кликнуть на кнопку закрытия окна с деталями ингредиента")
    def click_on_ingredient_details_close_button(self):
        self.click_on_element(self.locators.INGREDIENT_DETAILS_CLOSE_BUTTON)

    @allure.step("Переместить ингредиент «Флюоресцентная булка R2-D3» в корзину")
    def move_r2_d3_bun_to_basket(self):
        self.drag_and_drop_element(self.locators.R2_D3_BUN_BUTTON, self.locators.CONSTRUCTOR_BASKET)

    @allure.step("Подождать появления ингредиента «Флюоресцентная булка R2-D3 верх» в корзине")
    def wait_visibility_of_r2_d3_bun_top_in_basket(self):
        return self.wait_visibility_of_element(self.locators.R2_D3_BUN_TOP)

    @allure.step("Подождать появления ингредиента «Флюоресцентная булка R2-D3 низ» в корзине")
    def wait_visibility_of_r2_d3_bun_bottom_in_basket(self):
        return self.wait_visibility_of_element(self.locators.R2_D3_BUN_BOTTOM)

    @allure.step("Получить текст счетчика ингредиента «Флюоресцентная булка R2-D3»")
    def get_text_of_r2_d3_bun_counter(self):
        return self.get_text_of_element(self.locators.R2_D3_BUN_COUNTER)

    @allure.step("Подождать появления номера заказа")
    def wait_visibility_of_order_number(self):
        return self.wait_visibility_of_element(self.locators.ORDER_NUMBER_IN_CONSTRUCTOR)

    @allure.step("Получить номер заказа")
    def get_order_number(self):
        return self.get_text_of_element(self.locators.ORDER_NUMBER_IN_CONSTRUCTOR)

    @allure.step("Подождать исчезновения модального окна")
    def wait_invisibility_of_overlay(self):
        return self.wait_invisibility_of_element(self.locators.OVERLAY)