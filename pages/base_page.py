from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import allure

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def click_on_element(self, locator):
        with allure.step(f"Кликнуть на элемент {locator}"):
            self.driver.find_element(*locator).click()

    def wait_visibility_of_element(self, locator):
        with allure.step(f"Подождать видимость элемента {locator}"):
            return WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(locator))

    def wait_invisibility_of_element(self, locator):
        with allure.step(f"Подождать невидимость элемента {locator}"):
            return WebDriverWait(self.driver, 5).until(expected_conditions.invisibility_of_element(locator))

    def wait_clickability_of_element(self, locator):
        with allure.step(f"Подождать кликабельность элемента {locator}"):
            return WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(locator))

    def get_text_of_element(self, locator):
        with allure.step(f"Получить текст элемента {locator}"):
            return self.driver.find_element(*locator).text

    def fill_input(self, locator, text):
        with allure.step(f"Заполнить поле {locator}"):
            self.driver.find_element(*locator).send_keys(text)

    def drag_and_drop_element(self, source, target):
        with allure.step(f"Взять элемент {source} и передвинуть в {target}"):
            drag_and_drop_script = """
             function triggerDragAndDrop(source, target) {
                 const dataTransfer = new DataTransfer();

                 source.dispatchEvent(new DragEvent('dragstart', {
                     dataTransfer: dataTransfer,
                     bubbles: true
                 }));

                 target.dispatchEvent(new DragEvent('dragenter', {
                     dataTransfer: dataTransfer,
                     bubbles: true
                 }));

                 target.dispatchEvent(new DragEvent('dragover', {
                     dataTransfer: dataTransfer,
                     bubbles: true
                 }));

                 target.dispatchEvent(new DragEvent('drop', {
                     dataTransfer: dataTransfer,
                     bubbles: true
                 }));

                 source.dispatchEvent(new DragEvent('dragend', {
                     dataTransfer: dataTransfer,
                     bubbles: true
                 }));
             }

             triggerDragAndDrop(arguments[0], arguments[1]);
         """
            source = self.driver.find_element(*source)
            target = self.driver.find_element(*target)
            self.driver.execute_script(drag_and_drop_script, source, target)