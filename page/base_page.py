from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element_with_wait(self, locator):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    def wait_element_invisibility(self, wait_locator):
        WebDriverWait(self.driver, 30).until(expected_conditions.invisibility_of_element_located(wait_locator))

    def click_to_element(self, locator):
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(locator))
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].click();", element)

    def add_text_to_element(self, locator, text):
        self.find_element_with_wait(locator).send_keys(text)

    def get_text_from_element(self, locator):
        return self.find_element_with_wait(locator).text

    def drag_and_drop_element(self, locator_element, locator_target):
        ingredient = self.driver.find_element(*locator_element)
        basket_lst = self.driver.find_element(*locator_target)
        self.driver.execute_script(
            """
            const source = arguments[0];        
            const target = arguments[1];
                        
            const dataTransfer = new DataTransfer();
            const dragStartEvent = new DragEvent('dragstart', { bubbles: true, cancelable: true, dataTransfer });
            source.dispatchEvent(dragStartEvent);
            
            const dragOverEvent = new DragEvent('dragover', { bubbles: true, cancelable: true, dataTransfer });
            target.dispatchEvent(dragOverEvent);
            
            const dropEvent = new DragEvent('drop', { bubbles: true, cancelable: true, dataTransfer });        
            target.dispatchEvent(dropEvent);
            
            const dragEndEvent = new DragEvent('dragend', { bubbles: true, cancelable: true, dataTransfer });
            source.dispatchEvent(dragEndEvent);        
            """,
            ingredient,
            basket_lst
        )
