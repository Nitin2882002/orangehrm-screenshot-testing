import os
import allure
from selenium import webdriver
import time

def test_login_page():
    # Start WebDriver
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://opensource-demo.orangehrmlive.com/")

    time.sleep(2)

    # Screenshot path (use raw string to avoid \ errors)
    screenshot_path = r"C:\Users\ASUS\Desktop\orange hrm Project for 19\Full Automation\Screenshot_orangehrmAllurereprts\login_page.png"

    # Ensure folder exists
    os.makedirs(os.path.dirname(screenshot_path), exist_ok=True)

    # Save screenshot
    driver.save_screenshot(screenshot_path)

    # Attach screenshot to Allure report
    allure.attach.file(screenshot_path, name="Login Page Screenshot", attachment_type=allure.attachment_type.PNG)

    driver.quit()
