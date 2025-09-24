import pytest
import pytest_check as check
import allure

from pages.initial_loading_page import InitialLoadingPage
from pages.guest_home_page import GuestHomePage
from pages.home_page import HomePage
from pages.login_page import LogInPage



@pytest.mark.usefixtures("driver_setup", "test_data")
class TestDemoApp:

    @pytest.fixture(autouse=True, scope="class")
    def setup_class(cls, request, driver_setup):
        cls = request.cls
        cls.driver = driver_setup
        cls.initial_load_page = InitialLoadingPage(cls.driver)
        cls.guest_home_page = GuestHomePage(cls.driver)
        cls.login_page = LogInPage(cls.driver)
        cls.home_page = HomePage(cls.driver)


    @allure.description(
        "Given       User opens the iFarmer mobile application\n"
        "Then        Permission Dialog opens\n"
        "When        Click on Allow\n"
        "Then        Modal opens\n"
        "When        Click on cross button\n"
        "Then        On the iFarmer Home as a guest user\n"
    )
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.e2e
    def test_case_01_loading_guest_homepage(self, test_data):
        with allure.step("Test Permission Dialog"):
            check.is_true(self.initial_load_page.check_dialog(), "No Permission Dialog displayed") 
        with allure.step("Test Initial Modal"):
            check.is_true(self.initial_load_page.check_welcome_popup(), "No Welcome Popup window")
            

    @allure.description(
        "Given       User is on the iFarmer Home as a guest user\n"
        "When        Click on Login Nav\n"
        "Then        On the Login Page\n"
        "When        Enter valid email and pin\n"
        "And         Click on Login button\n"
        "Then        On the iFarmer Home as a logged in user\n"
    )
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.e2e
    def test_case_02_login_valid_user(self, test_data):
        with allure.step("Test Navigate to Login from Guest Home Page"):
            check.is_true(self.login_page.nav_login_from_guest(), "Could not navigate to Login from Guest Home Page") 
        with allure.step("Test Login with valid user"):
            check.is_true(self.login_page.login(test_data["login"]["email"], test_data["login"]["pin"]), "Could not login with valid user")
