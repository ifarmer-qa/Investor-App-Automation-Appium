from pages.element_handler import BasePage
import allure

class InitialLoadingPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        # Dialog Locators
        self.permission_dialog = (self.id_locator,"com.android.permissioncontroller:id/grant_dialog")
        self.dialog_message = (self.css_locator, "android.widget.TextView")
        self.dialog_close = (self.id_locator, "com.android.permissioncontroller:id/permission_allow_button")

        # Modal Locators
        self.modal_dialog = (self.id_locator, "asia.ifarmer.investor.dev:id/modal_content_root")
        self.modal_title = (self.id_locator, "asia.ifarmer.investor.dev:id/message_title")
        self.modal_body = (self.id_locator, "asia.ifarmer.investor.dev:id/message_body")
        self.modal_close = (self.css_locator, "android.widget.Button")

    
    
    def check_dialog(self):
        try:
            element = self.get_element(*self.permission_dialog)
            
            if element:
                self.text_log("Dialog has been Found", "check Dialog")

                message_element = self.find_child_element(element, *self.dialog_message)
                message = self.get_text(message_element) if message_element else "No message found"
                self.text_log(f"Dialog: {message}", "Check Dialog Message")

                self.take_screenshot(f"Dialog Showing")
                self.click(self.get_element(*self.dialog_close))
                self.take_screenshot(f"After Allowing Dialog")
                return True
            else:
                self.text_log("No Dialog has been Found", "check Dialog")
                return False
            
        except Exception as e:
            self.text_log(f"Error:\n{e}", "Error checking Dialog")
            return False
    
    

    def check_welcome_popup(self):
        try:
            element = self.get_element(*self.modal_dialog)
            if element:
                self.text_log("Modal has been Found", "check Modal")

                title_element = self.get_element(*self.modal_title)
                title= self.get_text(title_element) if title_element else "No Title found"
                body_element = self.get_element(*self.modal_body)
                message_body = self.get_text(body_element) if body_element else "No message found"
                self.text_log(f"Modal Title: {title}", "Check Modal Title")
                self.text_log(f"Modal Body: {message_body}", "Check Modal Body")

                self.take_screenshot(f"Modal Showing")
                self.click(self.get_element(*self.modal_close))
                self.take_screenshot(f"After Closing Modal")
                return True
            else:
                self.text_log("No Modal has been Found", "check Modal")
                return False
        
        except Exception as e:
            self.text_log(f"Error:\n{e}", "Error checking Modal")
            return False