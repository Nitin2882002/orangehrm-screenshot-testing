import allure

# Example usage inside a test case
def test_login_page(driver):  # assuming driver is your WebDriver fixture
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.save_screenshot("C:/Users/ASUS\Desktop/orange hrm Project for 19/Full Automation/Screenshot_orangehrmAllurereprts/login_page.png")
    allure.attach.file("screenshots/login_page.png", name="Login Page Screenshot", attachment_type=allure.attachment_type.PNG)
