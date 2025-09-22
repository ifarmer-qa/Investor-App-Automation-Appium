from pages.element_handler import BasePage
import allure

class GuestHomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        # User Locators
        self.user_locator = (self.accessibility_id_locator,"Good Evening\nGuest User")
        
    @allure.step("check Guest User")
    def check_guest_user(self):
        try:
            element = self.get_element(*self.user_locator)

            if element:
                self.text_log("This is Guest User Homepage.", "Guest Home")
                self.take_screenshot(f"Guest Home")
                return True
            
            else:
                self.text_log("This is not Guest User Homepage. Expect Guest Home.", "Not Guest Home")
                self.take_screenshot(f"Not Guest Home")
                return False
            
        except Exception as e:
            self.text_log(f"Error:\n{e}", "Error checking Guest Home Page")
            return False
    
            


