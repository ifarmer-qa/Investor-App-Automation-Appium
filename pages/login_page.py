from pages.element_handler import BasePage
import allure

class LogInPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        # Nav Locators
        self.login_nav = (self.accessibility_id_locator,"Login\nLogin\nTab 4 of 4")

        # LogIN page Locators
        self.email_input = (self.xpath_locator,"//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.EditText[1]")
        self.pin = (self.xpath_locator,"")





    def nav_login_from_guest(self):
        try:
            nav_login = self.get_element(*self.login_nav)

            if nav_login:
                self.click(nav_login)



    def login(self, email, pin)
        try:
