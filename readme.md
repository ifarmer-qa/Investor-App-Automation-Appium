<center>

# <strong>Investor App Automation Framework</strong>

<br>

# Test Automation Framework Setup (Python + Appium + Pytest)

<br>

![Python](https://img.shields.io/badge/python-3.9%2B-blue.svg) 
![Pytest](https://img.shields.io/badge/tested%20with-pytest-green.svg) 
![Appium](https://img.shields.io/badge/Appium-2.x-purple.svg) 
![Allure](https://img.shields.io/badge/Allure-Reporting-orange.svg) 



This repository provides a ready-to-use test automation framework for mobile and web apps using **Appium**, **Pytest**, and **Allure reporting**. 
</center>

<br>

# Table of Contents
<a name="top"></a>

1. [Project Description](#1-project-description)
2. [Framework Overview](#2-framework-overview)
3. [Project Structure](#3-project-structure)
4. [Error Handling & Assertions](#4-error-handling--assertions)
5. [Reporting & Archives](#5-reporting--archives)
6. [Scalability & Maintainability](#6-scalability--maintainability)
7. [Contribution Guidelines](#7-contribution-guidelines)
8. [System Requirements & Tools Installation](#8-system-requirements--tools-installation)
9. [Setup Virtual Environment & Install Dependencies](#9-setup-virtual-environment--install-dependencies)
10. [Running the Tests](#10-running-the-tests)
11. [Understanding Reports](#11-understanding-reports)
12. [Publishing Reports via GitHub Pages](#12-publishing-reports-via-github-pages)
13. [Summary & Best Practices](#13-summary--best-practices)



<br><br><br>

## 1. Project Description

This is a **mobile app automation framework** built using **Python, Appium, and Pytest**, with **Allure reporting** integrated.  
It is designed to automate the **iFarmer Investor Stage APK**, providing an organized, scalable, and maintainable approach for mobile test automation.  

**Key Features:**
- Easy-to-understand **Page Object Model (POM)** structure for all screens/pages.
- **Dynamic test data handling** using JSON files.
- Built-in **error handling and logging** integrated with Allure reports.
- **Automatic report generation and archiving** for test runs.
- Designed for **scalability** to handle multiple modules and complex test scenarios.
- Supports future **CI/CD integration**.

<br><br><br>

## 2. Framework Overview

The framework follows a **modular design** to ensure code reusability, maintainability, and scalability.  

<br>

### Core Components:

1. **Pages (`pages/`)**
   - Implements the **Page Object Model**.
   - Each page class represents a screen in the app.
   - Contains **locators, actions, and validations**.
   - Example pages: `GuestHomePage`, `HomePage`, `InitialLoadingPage`, `LoginPage`.

2. **Utilities (`utilities/`)**
   - Contains **helper functions** such as JSON loader, directory cleanup, folder copy, and other reusable utilities.

3. **Tests (`tests/`)**
   - Contains **Pytest test suites**.
   - Test classes are organized by functionality or feature.
   - Supports **fixtures** for setup/teardown and driver initialization.

4. **Resources (`resources/`)**
   - Stores **test data**, **Appium capabilities**, and **configuration files**.

5. **Driver Setup (`conftest.py`)**
   - Centralized **Appium driver setup** and teardown.
   - Defines session-level **fixtures** for test data and driver.
   - Automatically clears previous reports before execution.

6. **Reporting**
   - Integrated with **Allure reports**.
   - Generates **HTML reports**, archives raw results, and serves them automatically after test execution.

<br>

### Key Principles:

- **Separation of Concerns:** UI locators, test logic, and test data are separated for maintainability.
- **Dynamic and Reusable Code:** Base classes and utility methods reduce duplication.
- **Automation Ready:** Designed to support multiple devices and future CI/CD pipelines.

<br>

[🔝 Back to Top](#top)

<br><br><br>

## 3. Project Structure

The framework follows a clear and organized folder structure to ensure **maintainability, scalability, and readability**.  

Here’s the current structure:

```text
.
├── 📁 apk
│   └── 📱 inv_stage.apk
├── 📁 resources
│   ├── ⚙️ capabilities.json
│   └── 📝 test_data.json
├── 📁 pages
│   ├── 🐍 element_handler.py
│   ├── 🐍 guest_home_page.py
│   ├── 🐍 home_page.py
│   ├── 🐍 initial_loading_page.py
│   └── 🐍 login_page.py
├── 📁 tests
│   └── 🧪 test_suite_01.py
├── 📁 utilities
│   └── 🛠️ utility.py
├── 🐍 conftest.py
├── ⚙️ pytest.ini
└── ⚙️ requirements.txt
```


<br>

### Folder & File Descriptions

- **`📁 apk/`**
  - Stores the APK file(s) used for testing.
  - Example: `📱 inv_stage.apk` is the Investor Stage APK.

  - **`📁 resources/`**
  - Stores **config files, test data, and capabilities**.
  - Key files:
    - `⚙️ capabilities.json` → Appium capabilities for the target device.
    - `📝 test_data.json` → Dynamic test data for tests.

- **`📁 pages/`**
  - Implements the **Page Object Model (POM)**.
  - Each file represents a page/screen in the app.
  - Includes locators, actions, and validations.
  - **Key files:**
    - `🐍 element_handler.py` → Base class for reusable actions (click, enter_text, wait, screenshot).
    - `🐍 guest_home_page.py` → Guest homepage-specific actions and validations.
    - `🐍 home_page.py` → Main user homepage (structure similar to guest home page).
    - `🐍 initial_loading_page.py` → Handles dialogs, modals, and initial app popups.
    - `🐍 login_page.py` → Handles login functionality (future implementation).

- **`📁 tests/`**
  - Contains all **Pytest test cases**.
  - Example: `🧪 test_suite_01.py` demonstrates **initial loading flow** and **guest home page validation**.
  - Supports fixtures from `🐍 conftest.py`.

- **`📁 utilities/`**
  - Helper functions and utility methods used across the framework.
  - Example: `🛠️ utility.py` → Functions for **JSON loading, folder cleanup, and folder copy**.

  - **`🐍 conftest.py`**
  - Handles **Appium driver setup/teardown**.
  - Contains **Pytest fixtures** for driver and test data.
  - Clears old reports before execution and generates Allure reports after test runs.

  - **`⚙️ pytest.ini`**
  - Pytest configuration file.
  - Configures **markers**, **logging**, and **report options**.

  - **`⚙️ requirements.txt`**
  - Lists all Python dependencies with pinned versions.
  - Ensures reproducible environment for anyone cloning the repository.

<br>

### Notes:

- The framework is designed so new pages can be added by simply creating a new file in the `📁 pages/` folder and inheriting from `🧩 BasePage`.
- New test cases can be added in the `📁 tests/` folder, using the **fixtures** and page objects already defined.
- All dynamic configurations (like capabilities or test data) are kept in the `📁 resources/` folder to **avoid hardcoding**.

<br>

[🔝 Back to Top](#top)

<br><br><br>

## 4. Error Handling & Assertions

This framework follows **robust error handling and assertion practices** to ensure reliable and maintainable test execution.  

<br>

### Error Handling

1. **Centralized Error Logging**
   - All errors or exceptions encountered during execution are **captured** and **logged** with **Allure attachments**.
   - The `🧩 BasePage` class (`🐍 element_handler.py`) provides helper methods:
     - `take_screenshot(step_name)` → Captures a screenshot and attaches it to the Allure report.
     - `text_log(text, step_name)` → Attaches plain text messages to the Allure report.
   - Example:

     ```python
     try:
         element = self.get_element(*self.permission_dialog)
     except Exception as e:
         self.text_log(f"Error:\n{e}", "Error checking Dialog")
     ```

2. **Implicit & Explicit Waits**
   - The framework uses **implicit waits** in the driver setup (`driver.implicitly_wait(3)`) to handle general loading delays.
   - For specific elements, **explicit waits** using `WebDriverWait` ensure the element is present before interacting.

3. **Safe Element Interaction**
   - Methods like `click()` and `enter_text()` include **pre-checks** and logging to prevent runtime exceptions.
   - Errors are caught and logged to avoid test crashes and to provide clear failure context.


<br>

### Assertions

1. **Pytest Assertions**
   - Standard `assert` statements are used in tests to validate expected outcomes.
   - Example:

     ```python
     product_text = self.home_page.get_products_text()
     assert product_text == "Products", f"Expected 'Products' but got {product_text}"
     ```

2. **Soft Assertions with `pytest-check`**
   - For scenarios where multiple validations are required in a single test, **soft assertions** allow tests to continue even if one check fails.
   - Example:

     ```python
     import pytest_check as check
     
     check.is_true(self.initial_load_page.check_dialog(), "No Permission Dialog displayed")
     check.is_true(self.initial_load_page.check_welcome_popup(), "No Welcome Popup window")
     ```

3. **Allure Integration**
   - Assertions are **logged in Allure** with steps and optional screenshots.
   - Provides **full context** for failed steps including the exact UI state and messages.


<br>

### Best Practices

- Always use the **BasePage helper methods** for interactions instead of raw driver calls.
- Wrap any risky operations in **try-except blocks** to attach errors to the report.
- Use **soft assertions** for multi-step validations where failure of one step should not halt the test.
- Attach **screenshots and descriptive logs** for every critical step to make debugging easier.

<br>

[🔝 Back to Top](#top)

<br><br><br>

## 5. Reporting & Archives

The framework uses **Allure reporting** integrated with Pytest to provide **detailed, visual, and actionable test reports**.  

<br>

### Report Generation

1. **Automatic Allure Report**
   - At the end of each test session, the framework automatically:
     - Generates the **latest Allure report**.
     - Archives the raw results for future reference.
     - Serves the report locally for immediate review.
   - This is handled in `🐍 conftest.py` using:

     ```python
     os.system(f"allure generate {ltst_result} -o {ltst_report} --clean")
     os.system(f"allure serve {ltst_result}")
     ```

2. **Allure Attachments**
   - Screenshots, logs, and text messages are attached to the report dynamically.
   - `🧩 BasePage` methods for attachments:
     - `take_screenshot(step_name)`
     - `text_log(text, step_name)`

3. **Steps in Reports**
   - Allure steps are used for **clarity and traceability** in test execution:

     ```python
     with allure.step("Test Permission Dialog"):
         check.is_true(self.initial_load_page.check_dialog(), "No Permission Dialog displayed")
     ```

<br>

### Archiving Strategy

1. **Structured Archiving**
   - Each test run creates a **date/time-based folder** for raw results and generated reports:

    ```
    📁 reports
    └── 📁 INVESTOR_STAGE_Archive
        └── 📁 YYYY_MM_DD
            └── 📁 HH_MM
                ├── 📁 raw_result
                └── 📁 serve_report
    ```

   - Keeps **previous runs intact** for traceability.

2. **Latest Reports**
   - `reports/allure-latest-results/` → Latest raw results for immediate use.
   - `reports/allure-latest-report/` → Latest served report for review.

3. **Automatic Cleanup**
   - Before a new test session, the framework clears old results and reports to avoid confusion:

     ```python
     ut.clear_directory(f"{ltst_result}")
     ut.clear_directory(f"{ltst_report}")
     ```

<br>

### Benefits

- **Immediate Feedback:** Developers and QA can review results right after tests.
- **Visual Logs:** Screenshots and step-by-step logs make debugging easier.
- **Historical Record:** Archived reports provide traceability for all past test runs.
- **CI/CD Ready:** Reports can be integrated into pipelines for automated visibility.


<br>

### Recommendations

- Always check the **serve report** after test execution for interactive steps and logs.
- Keep archived reports for **long-term tracking** of regression test runs.
- Use descriptive step names to **enhance report readability**.

<br>

[🔝 Back to Top](#top)

<br><br><br>

## 6. Scalability & Maintainability

This framework is designed to be **scalable, modular, and easy to maintain**, even as the application under test grows in complexity.  

<br>

### Key Principles for Scalability

1. **Page Object Model (POM)**
   - Each screen of the application has its own page class in the `📁 pages/` folder.
   - All UI actions and validations are encapsulated in these classes.
   - To add a new page:
     - Create a new file in `📁 pages/`.
     - Inherit from `🧩 BasePage`.
     - Define locators and actions for the new page.

2. **Reusable Utility Functions**
   - Utility methods in `📁 utilities/🐍 utility.py` handle common operations such as:
     - JSON data loading
     - Directory cleanup
     - Folder copying
   - Reduces duplication across tests.

3. **Dynamic Test Data**
   - Test data is stored in `📁 resources/📝 test_data.json`.
   - Tests read input dynamically, enabling **data-driven testing**.
   - Adding new scenarios only requires updating the JSON file, without changing the code.

4. **Driver & Fixture Reuse**
   - `🐍 conftest.py` defines **session-level and package-level fixtures**.
   - Single driver instance can be shared across multiple test classes for efficiency.

5. **Soft Assertions & Error Handling**
   - Allows multiple validations per test without stopping execution.
   - Errors and exceptions are logged in Allure with screenshots, aiding debugging.


<br>

### Maintainability Tips

1. **Organize Tests by Feature**
   - Place tests in the `📁 tests/` folder grouped by **Test Suite**.
   - Example:

     ```
     📁 tests
        ├── 🧪 test_suite_01.py
        ├── 🧪 test_suite_02.py
        ├── 🧪 test_suite_03.py
        └── ...
     ```

2. **Keep Locators Centralized**
   - Always define locators inside page classes.
   - Avoid hardcoding locators in test files.

3. **Descriptive Logging**
   - Use `take_screenshot()` and `text_log()` for every critical action.
   - Helps in understanding failures without checking the app manually.

4. **Version Control**
   - Maintain **branching strategy** to avoid breaking main tests (details in Contribution section).

5. **Code Reuse**
   - Always use base methods from `🧩 BasePage` for clicks, text entry, and waits.
   - Avoid duplicating logic in multiple page or test files.


<br>

### Adding New Features / Pages

1. **Create Page Class**
   - Inherit from `🧩 BasePage`.
   - Define locators and action methods.

2. **Update Test Data**
   - Add any necessary data to `📁 resources/📝 test_data.json`.

3. **Add Test Case**
   - Create a new test class in `📁 tests/`.
   - Use fixtures and page objects.
   - Attach logs and screenshots for Allure reporting.

4. **Run & Verify**
   - Execute the test.
   - Confirm Allure reports show correct steps and logs.

By following this structure, the framework can scale to **hundreds of tests** and **multiple app modules** without breaking.

<br>

[🔝 Back to Top](#top)

<br><br><br>

## 7. Contribution Guidelines

This section explains how to safely contribute to the framework without breaking existing tests.  

<br>

### Branching Strategy

1. **Main Branch**
   - `main` branch contains **stable and fully tested code**.
   - No direct commits should be made to `main`.

2. **Feature Branches**
   - For new tests or features, create a **feature branch**:

     ```bash
     git checkout -b feature/<feature-name>
     ```

   - Example: `feature/login-tests`

3. **Bugfix Branches**
   - For fixing bugs in existing tests or utilities:

     ```bash
     git checkout -b bugfix/<bug-name>
     ```

   - Example: `bugfix/dialog-handling`

4. **Pull Requests (PRs)**
   - Push your branch to the repository:

     ```bash
     git push origin feature/<feature-name>
     ```

   - Open a **Pull Request (PR)** targeting `main`.
   - PRs should be reviewed and **tests must pass** before merging.

<br>

### Contribution Approach

1. **Always Pull Latest Changes**
   - Before starting work, ensure your branch is up-to-date:

     ```bash
     git checkout main
     git pull origin main
     ```

2. **Implement Feature / Fix**
   - Add new pages in `📁 pages/` if needed.
   - Add new test cases in `📁 tests/`.
   - Update `📁 resources/📝 test_data.json` if required.

3. **Run All Tests Locally**
   - Execute all existing tests to ensure nothing breaks:

     ```bash
     pytest
     ```

4. **Follow Code Style**
   - Use **PEP8** compliant formatting.
   - Keep locators, actions, and test logic separated (Page Object Model).

5. **Use Descriptive Commit Messages**
   - Example:
   
     ```bash
     git commit -m "Added login page test cases with error handling"
     ```

6. **Attach Screenshots / Logs**
   - For Allure reporting, ensure critical steps have screenshots and logs using `BasePage` methods:
     - `take_screenshot(step_name)`
     - `text_log(text, step_name)`

<br>

### Best Practices

- Never commit broken code to `main`.
- Keep feature branches **small and focused**.
- Always test your changes locally before opening a PR.
- Document new test scenarios in **Allure steps** for clarity.

<br>

[🔝 Back to Top](#top)

<br><br><br>

## 8. System Requirements & Tools Installation

To run this mobile automation framework, the following tools and dependencies must be installed on your system.  

<br>

### Required Tools

1. **Python (>=3.10)**
   - Check Python version:

     ```bash
     python --version
     ```

   - Install Python:
     - **Windows:** Download from [Python.org](https://www.python.org/downloads/windows/) and add to PATH.
     - **macOS:** 

       ```bash
       brew install python
       ```

     - **Linux (Ubuntu/Debian):**

       ```bash
       sudo apt update
       sudo apt install python3 python3-pip
       ```

2. **Java (>=11)**
   - Required for Appium and Android SDK.
   - Check version:

     ```bash
     java -version
     ```

   - Install:
     - **Windows / macOS:** Download from [AdoptOpenJDK](https://adoptium.net/) and set `JAVA_HOME`.
     - **Linux (Ubuntu/Debian):**

       ```bash
       sudo apt install openjdk-11-jdk
       ```

3. **Node.js & NPM**
   - Required to run Appium server.
   - Check version:

     ```bash
     node -v
     npm -v
     ```

   - Install:
     - **Windows / macOS:** [Node.js Downloads](https://nodejs.org/en/download/)
     - **Linux (Ubuntu/Debian):**

       ```bash
       sudo apt install nodejs npm
       ```

4. **Appium**
   - Install globally via npm:

     ```bash
     npm install -g appium
     ```

   - Verify installation:

     ```bash
     appium -v
     ```

5. **Android SDK / Emulator**
   - Required for running Android tests.
   - Install Android Studio and configure `ANDROID_HOME`.
   - Add `platform-tools` to PATH.

6. **Allure Commandline**
   - Required for generating reports.
   - Install:
     - **Windows:** Download ZIP from [Allure Releases](https://github.com/allure-framework/allure2/releases), unzip, and add `bin` to PATH.
     - **macOS:**

       ```bash
       brew install allure
       ```

     - **Linux (Ubuntu/Debian):**

       ```bash
       sudo apt-add-repository ppa:qameta/allure
       sudo apt update
       sudo apt install allure
       ```

7. **Git**
   - Required for cloning repository and contribution.
   - Check version:

     ```bash
     git --version
     ```

   - Install:
     - **Windows:** [Git Downloads](https://git-scm.com/download/win)
     - **macOS:** 

       ```bash
       brew install git
       ```
     - **Linux (Ubuntu/Debian):**

       ```bash
       sudo apt install git
       ```

<br>

### Additional Tools (Optional)

- **Visual Studio Code / PyCharm**
  - For Python development.
- **Android Emulator / Real Device**
  - To run automated tests.

<br>

[🔝 Back to Top](#top)

<br><br><br>

## 9. Setup Virtual Environment & Install Dependencies

Follow these steps to create an isolated Python environment and install all required dependencies for the framework.

<br>

### Clone the Repository

```bash
git clone https://github.com/ifarmer-qa/Investor-App-Automation-Appium.git
cd Investor-App-Automation-Appium
```

<br>

### Create a Virtual Environment

```bash
# Windows
python -m venv venv

# macOS / Linux
python3 -m venv venv
```

<br>

### Activate the Virtual Environment 

```bash
# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate
```

> **Note:** After activating the virtual environment, your terminal should show `(venv)` at the start.

<br>

### Upgrade `pip` (Optional but Recommended)

```bash
pip install --upgrade pip
```

<br>

### Install All Dependencies   

```bash
pip install -r requirements.txt
```

- This will install all packages including:
    - Appium-Python-Client
    - pytest, pytest-check, pytest-html
    - selenium
    - allure-pytest
    - And other supporting libraries.

<br>

### Verify Installation

- **Check Python version:** 

    ```bash
    python --version
    ```

- **Check pip packages:** 

    ```bash
    pip list
    ```

- **Check Appium and Node.js:**

    ```bash
    appium -v
    node -v
    ```

<br>

### Ready to Run Tests

- Once the virtual environment is active and dependencies are installed, the framework is ready for test execution.

<br>

[🔝 Back to Top](#top)

<br><br><br>

## 10. Running the Tests

This section explains how to execute the automated tests, including pre-steps, commands, and considerations.

<br>

### Pre-Steps Before Running Tests

1. **Start Appium Server**
   - Make sure the Appium server is running before executing tests.
   - Command:

     ```bash
     appium
     ```

   - Verify if it is running on the default URL: `http://127.0.0.1:4723`
   - If the Appium server URL is different from the default, update it in `🐍 conftest.py` by modifying the global variable `appium_server_url`.


2. **Connect Android Device / Emulator**
   - Ensure your Android device is connected via USB with **Developer Options & USB Debugging enabled**, or an emulator is running.
   - Verify device with:

      ```bash
      adb devices
      ```

3. **Activate Virtual Environment**

    ```bash
    # Windows
    venv\Scripts\activate

    # macOS / Linux
    source venv/bin/activate
    ```

4. **Ensure APK is in Place**
    - The APK file should be in `📁 apk/` folder as specified in `⚙️ capabilities.json`.
    - Example: `📁 apk/📱 inv_stage.apk`

<br>

### Running All Tests

- To run all tests in the framework:

    ```bash
    pytest
    ```

- This will automatically:
    - Launch Appium driver
    - Execute tests in `📁 tests/` folder
    - Generate Allure results in `📁 reports/📁 allure-latest-results`
    - Serve the Allure HTML report

<br>

### Running Specific Test Suites or Files

- Run a single test file:

    ```bash
    pytest tests/test_suite_01.py
    ```

- Run tests with a specific marker (e.g., e2e):

    ```bash
    pytest -m e2e
    ```

<br>

### Generating Allure HTML Reports Manually (Optional)
- Generate a clean report from latest results:

    ```bash
    allure generate reports/allure-latest-results -o reports/allure-latest-report --clean
    ```

- Serve the report locally:

    ```bash
    allure serve reports/allure-latest-results
    ```

- Open the generated HTML report in a browser:

    ```bash
    allure open reports/allure-latest-report/
    ```

<br>

### Considerations

- Ensure no other Appium sessions are running to avoid driver conflicts.
- Always check `📁 resources/⚙️ capabilities.json` for correct deviceName, appPackage, and appActivity.
- For long test suites, the archive folder is automatically created:

    ```swift
    reports/INVESTOR_STAGE_Archive/YYYY_MM_DD/HH_MM/
    ```

- Screenshots and logs are attached automatically for failed and passed steps.

<br>

[🔝 Back to Top](#top)

<br><br><br>

## 11. Understanding Reports

The framework uses **Allure reporting** to provide detailed and interactive test reports.  
This section explains how to interpret the reports, view steps, logs, and attachments.

<br>

### Report Location

- **Latest generated Allure HTML Report:**

    ```swift
    reports/allure-latest-report/
    ```

- Open Allure HTML report in a browser:

    ```bash
    allure open reports/allure-latest-report/
    ```

- **Archived generated Allure HTML Reports:**

    ```swift
    reports/INVESTOR_STAGE_Archive/YYYY_MM_DD/HH_MM/serve_report/
    ```

- Open Archived Allure HTML report in a browser:

    ```bash
    allure open reports/INVESTOR_STAGE_Archive/YYYY_MM_DD/HH_MM/serve_report/
    ```

- Preserves historical results for traceability.

<br>

### Report Structure

Allure reports consist of:

1. **Test Suites**
 - Displays organized test suites and classes.
 - Click a suite to view **individual test cases**.

2. **Test Cases**
 - Each test case shows:
   - **Status:** Passed, Failed, or Skipped
   - **Duration:** Execution time
   - **Steps:** Step-by-step actions
   - **Attachments:** Screenshots, logs, or other files

3. **Steps**
 - All actions in a test are logged as **Allure steps**.
 - Example step:

   ```
   Test Permission Dialog → Passed
   Check Welcome Popup → Passed
   ```

 - Clicking a step shows details and any attached screenshots or text logs.

4. **Attachments**
 - Screenshots are captured for:
   - Successful critical steps
   - Failed steps
 - Text logs provide context, such as:

   ```
   Dialog: Permission Granted
   Modal Title: iFarmer
   Modal Body: iFarmer HQ
   ```


<br>

### Navigating the Report

- **Overview Tab:** Summary of test results, total tests, and trends.
- **Suites Tab:** Drill down into each test suite and its cases.
- **Graphs Tab:** Visual graphs for test trends and execution times.
- **Categories:** Quickly view failed, broken, or flaky tests.

<br>

### Best Practices

- Use **descriptive step names** in your tests for better clarity.
- Attach **screenshots for critical UI actions**.
- Always check **failed steps first** for quick debugging.
- Use archived reports to **compare test runs over time**.

<br>

[🔝 Back to Top](#top)

<br><br><br>

## 12. Publishing Reports via GitHub Pages

You can host Allure HTML reports on **GitHub Pages** to share with your team or stakeholders.
> Currently the framework will update the latest report on Github by default whenever it runs.

<br>

### Prepare the Allure Report

- **Generate the latest Allure report:**

    ```bash
    allure generate reports/allure-latest-results -o reports/allure-latest-report --clean
    ```

- **Verify that the report exists at:**

    ```bash
    allure open reports/allure-latest-report/
    ```

<br>

### Create a `gh-pages` Branch

- Create and switch to a `gh-pages` branch:

    ```bash
    git checkout --orphan gh-pages
    ```

- Remove existing files (optional if branch is empty):

    ```bash
    git rm -rf .
    ```

- Copy the generated Allure HTML report to the root of this branch:

    ```bash
    cp -r reports/allure-latest-report/* .
    ```

<br>

### Commit and Push

  ```bash
  git add .
  git commit -m "Publish latest Allure report"
  git push origin gh-pages
  ```

<br>

### Configure GitHub Pages

- Go to your repository on GitHub.
- Navigate to **Settings** → **Pages**.
- Under **Source**, select the `gh-pages` branch.
- Save settings. GitHub will provide a **URL** to access the report:

    ```markdown
    # Report URL for this Repo
    https://ifarmer-qa.github.io/Investor-App-Automation-Appium/

    #Basic Template for page URL
    https://<username>.github.io/<repository>/
    ```

<br>

### Updating Reports

- Whenever you generate a new report, repeat steps 1–3 to **push updated HTML files** to `gh-pages`.
- The GitHub Pages URL will always show the `latest report`.

<br>

[🔝 Back to Top](#top)

<br><br><br>

## 13. Summary & Best Practices

This section provides a concise overview of how to maintain, scale, and use the automation framework efficiently.

<br>

### Summary

- **Framework Design:**  
  - Follows **Page Object Model (POM)** for modularity.  
  - Dynamic test data and configuration stored in `resources/` for flexibility.  
  - Utilities in `utilities/` provide reusable helper functions.

- **Error Handling & Assertions:**  
  - Centralized error logging with Allure attachments.  
  - Soft assertions allow multiple validations per test.  
  - Screenshots and text logs help debug failed steps quickly.

- **Reporting & Archives:**  
  - Allure reports provide interactive and detailed test results.  
  - Each test run is archived by date/time for traceability.  
  - Latest results are always available in `reports/allure-latest-report`.

- **Contribution Guidelines:**  
  - Use feature/bugfix branches to avoid breaking main.  
  - Always test changes locally and follow code standards.  
  - Use descriptive commit messages and document Allure steps.

- **System Setup & Dependencies:**  
  - Python, Java, Node.js, Appium, Android SDK, Git, and Allure are required.  
  - Virtual environments ensure isolated and reproducible setups.

- **Execution:**  
  - Tests can be executed via `pytest`.  
  - Reports are automatically generated and can be served locally or published to GitHub Pages.

<br>

### Best Practices for Efficient Use

1. **Organize Tests by Feature/Module**
   - Helps locate and maintain tests efficiently.  
   - Example folder structure in `tests/`:

    ```
    📁 tests
    ├── 🧪 test_suite_01.py
    ├── 🧪 test_suite_02.py
    ├── 🧪 test_suite_03.py
    └── ...
    ```

2. **Use Page Object Methods**
   - Always interact with UI elements via `BasePage` methods (`click`, `enter_text`, `take_screenshot`).  
   - Avoid direct driver calls in test files.

3. **Descriptive Logging**
   - Attach screenshots and logs for every critical step.  
   - Use Allure steps for readability in reports.

4. **Dynamic Test Data**
   - Keep test data in `📁 resources/📝 test_data.json`.  
   - Avoid hardcoding values inside tests.

5. **Version Control Discipline**
   - Follow branch and PR strategies to avoid breaking the framework.  
   - Test locally before merging.

6. **Regular Maintenance**
   - Update dependencies in `⚙️ requirements.txt` periodically.  
   - Review and refactor page objects when UI changes.  
   - Remove obsolete test cases and archived reports periodically.

7. **Scalability Tips**
   - Add new pages or utilities modularly.  
   - Use fixtures for shared resources like drivers and test data.  
   - Implement CI/CD integration for automatic execution and report publishing.

<br>

### Framework Advantages

- **Modular & Scalable:** Easy to add new pages, test cases, and modules.  
- **Dynamic & Maintainable:** Test data and capabilities are configurable without code changes.  
- **Clear Reporting:** Allure reports with screenshots, logs, and step tracking.  
- **Collaboration-Friendly:** Git workflow ensures safe contributions from multiple developers.  
- **CI/CD Ready:** Supports automated execution and report publishing.

<br>

[🔝 Back to Top](#top)

<br><br>
<br><br>
<br><br>
<br><br>

# <p align="center">✨ <strong>Happy Testing! May your bugs be few and your automation stable!</strong> 🚀</p>

<br><br>