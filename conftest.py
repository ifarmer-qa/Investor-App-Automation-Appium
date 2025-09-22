import pytest
import os
from appium import webdriver
from appium.options.common.base import AppiumOptions
from utilities import utility as ut
from datetime import datetime

appium_server_url = "http://127.0.0.1:4723"


current_time = datetime.now()
time = current_time.strftime("%H_%M")
date = current_time.strftime("%m_%d_%Y")
archive_path = f"reports/INVESTOR_STAGE_Archive/{date}/{time}"
result_archive = f"{archive_path}/raw_result"
report_archive = f"{archive_path}/serve_report"
ltst_result = f"reports/allure-latest-results"
ltst_report = f"reports/allure-latest-report"


def pytest_sessionstart(session):
    """Clear directories before the test session starts."""
    ut.clear_directory(f"{ltst_result}")        # Clear previous allure-latest-results directories
    ut.clear_directory(f"{ltst_report}")         # Clear previous allure-latest-report directories


@pytest.fixture(scope="session")
def test_data():
    """Load test data from JSON file."""
    return  ut.load_json('resources/test_data.json')



# Setup fixture for Appium driver
@pytest.fixture(scope="package")
def driver_setup(request):
    """Setup Appium driver and capabilites."""

    options = AppiumOptions()       # Create appium options
    options.load_capabilities(ut.load_json('resources/capabilities.json'))      # Extract values from the json file and assign them to the options
    
    driver = webdriver.Remote(appium_server_url, options = options)     # Create the Appium driver
    driver.implicitly_wait(3)
    
    yield driver    # yield the driver to the test
    driver.quit()   # Close the Appium driver




def pytest_sessionfinish(session, exitstatus):
    """Generate Allure reports automatically after test run"""
    os.system(f"allure generate {ltst_result} -o {ltst_report} --clean")        # Generate Allure report
    os.system(f"allure generate {ltst_result} -o {report_archive} --clean")
    ut.copy_folder(ltst_result, result_archive)
    os.system(f"allure serve {ltst_result}")        # Serve Allure report