from pages.element_handler import BasePage
import allure

class LogInPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        # Nav Locators
        self.login_nav = (self.accessibility_id_locator,"Login\nLogin\nTab 4 of 4")

        # LogIN page Locators
        self.email_input = (self.xpath_locator,"//*[@content-desc='Email']/following-sibling::android.widget.EditText[1]")
        self.pin_input = (self.xpath_locator,"//*[@content-desc='PIN']/following-sibling::android.widget.EditText[1]")
        self.login_button = (self.accessibility_id_locator,"Login")



    def nav_login_from_guest(self):
        try:
            nav_login = self.get_element(*self.login_nav)

            if nav_login:
                self.text_log("Login Nav found", "Login Nav")
                self.take_screenshot("Login Nav found")
                self.click(nav_login)
                return True
            else:
                self.text_log("Login Nav not found", "Login Nav")
                self.take_screenshot("Login Nav not found")
                return False    

        except Exception as e:
            self.text_log(f"Error:\n{e}", "Error getting Login Nav")
            return False


    def login(self, email, pin):
        try:
            email_input = self.get_element(*self.email_input)
            if email_input:
                self.text_log("Email input found", "Email input")
                self.take_screenshot("Email input found")
                self.enter_text(email_input, email)
                self.take_screenshot("Email entered")
            else:
                self.text_log("Email input not found", "Email input")
                self.take_screenshot("Email input not found")
                return False

            pin_input = self.get_element(*self.pin_input)
            if pin_input:
                self.text_log("PIN input found", "PIN input")
                self.take_screenshot("PIN input found")
                self.enter_text(pin_input, pin)
                self.take_screenshot("PIN entered")
            else:
                self.text_log("PIN input not found", "PIN input")
                self.take_screenshot("PIN input not found")
                return False

            login_button = self.get_element(*self.login_button)
            if login_button:
                self.text_log("Login button found", "Login button")
                self.click(login_button)
                self.take_screenshot("Login button clicked")
                return True
            else:
                self.text_log("Login button not found", "Login button")
                self.take_screenshot("Login button not found")
                return False

        except Exception as e:
            self.text_log(f"Error:\n{e}", "Error logging in")
            return False

