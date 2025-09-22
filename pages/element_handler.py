from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.xpath_locator = AppiumBy.XPATH
        self.accessibility_id_locator = AppiumBy.ACCESSIBILITY_ID
        self.id_locator = AppiumBy.ID
        self.css_locator = AppiumBy.CLASS_NAME

    def click(self, element):
        element.click()
        self.driver.implicitly_wait(1)

    def enter_text(self, element, text):
        element.clear()
        element.send_keys(text)
        self.driver.implicitly_wait(1)

    def get_text(self, element):
        return element.text
    
    def get_element(self, locator_type, locator):
        element = self.wait_for_element((locator_type, locator)) #self.driver.find_element(locator_type, locator)
        return element
    
    def find_child_element(self, parent_element, locator_type, locator):
        self.driver.implicitly_wait(1)
        element = parent_element.find_element(locator_type, locator)
        return element
    
    def wait_for_element(self, element, timeout=15):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(element)
        )
    

    def take_screenshot(self, step_name):
        #with allure.step(f"Screenshot: {step_name}"):
        screenshot = self.driver.get_screenshot_as_png()
        allure.attach(screenshot, name=step_name, attachment_type=allure.attachment_type.PNG)

    def text_log(self, text, step_name):
        allure.attach(text, name=step_name, attachment_type=allure.attachment_type.TEXT)