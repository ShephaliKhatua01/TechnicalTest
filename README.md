# Project Overview
**This documentation provides an overview of the automated testing project for the website https://www.demoblaze.com/. The project uses Python and Selenium WebDriver for automating various test scenarios on the website.**

GitHub Repository: https://github.com/ShephaliKhatua01/TechnicalTest

# 1. Introduction
This automated testing project aims to ensure the reliability and functionality of the https://www.demoblaze.com/ website by automating test scenarios using Python and Selenium WebDriver.

# 2. Test Scenarios
The project currently covers the following test scenarios: (and further tese cases will be added) 

1. Login: Ability to log in
2. Add to Cart: Ability to add an item to the cart
3. Place an Order: Ability to place an order from the cart page and complete a purchase

# 3. Setup and Prerequisites
Before running the tests, ensure you have the following prerequisites installed:

1. Python
2. Selenium WebDriver
3. Web driver executable (e.g., ChromeDriver)
4. PyCharm (IDE) (Optional)

**1. Installation**

Clone the GitHub repository:
git clone https://github.com/ShephaliKhatua01/TechnicalTest.git


**2. Install Selenium WebDriver:**

pip install selenium

**3. Download the appropriate web driver executable** (e.g., ChromeDriver) and add it to your system's PATH.

# 4. Project Structure
The project's file structure is organized as follows:

1. chromedriver: The web driver executable (update with your preferred driver).
2. e2e_test_script.py: Python script containing the automated test cases.
3. ExecuteE2ETest.py: Python script containing the parametarized test function to execute test script with diff data set.
4. POM -For reference Page Object Model struture started for above mentioned scenarios and will continue in future. (Login scenario is completed, check file login_test.py )
     1. Page dir - To store locators and actions of the web-elements.
     2. Test dir - Script for automated scenarios.
6. README.md: Project documentation (you're reading it now).

# 6. Adding New Test Cases
To add new test cases in the future:

1. Create a new test function in e2e_test_script.py.
2. Implement the test logic within the function.
3. Add function with required parameter in ExecuteE2ETest.py and execute.
4. Update the documentation in the "Test Scenarios" section to indicate the new test case's status.
5. Encourage contributors to add meaningful comments to the code for clarity.

 # 7. Contributing
Contributions to this project are welcome. If you want to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch for your changes.
3. Make your changes and commit them with descriptive commit messages.
4. Create a pull request to merge your changes.

# 8. Contact
For any questions or concerns regarding this project, please contact the project owner:

Name: Shephali Khatua
Email: shephali.khatua@gmail.com

