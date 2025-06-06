
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
import os
from dotenv import load_dotenv


def automate_discord_login_flow(url):
    # override=True forces dotenv to overwrite existing system variables.
    load_dotenv(override=True)

    # Both credentials are now loaded from the .env file
    email_address = os.getenv('USERNAME')
    password = os.getenv('PASSWORD')

    if not email_address or not password:
        print("Error: 'USERNAME' or 'PASSWORD' not found or is empty in the .env file.")
        print("Please ensure your .env file is configured correctly (USERNAME=..., PASSWORD=...).")
        return None

    driver = None
    try:
        print("Initializing Chrome WebDriver...")
        service = webdriver.ChromeService(ChromeDriverManager().install())
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(service=service, options=options)

        print(f"Opening webpage directly: {url}...")
        driver.get(url)

        # --- Step 1: Enter Email ---
        try:
            print("Waiting for the email input field...")
            email_input_field = WebDriverWait(driver, 15).until(
                EC.visibility_of_element_located((By.NAME, "email"))
            )
            email_input_field.send_keys(email_address)
            print(f"Username '{email_address}' from .env file entered.")
            time.sleep(1)
        except Exception as e:
            print(f"Email input field not found: {e}")
            if driver: driver.quit()
            return None

        # --- Step 2: Enter Password ---
        try:
            print("Waiting for the password input field...")
            password_input_field = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.NAME, "password"))
            )
            password_input_field.send_keys(password)
            print("Password from .env file entered.")
            time.sleep(1)
        except Exception as e:
            print(f"Password input field not found: {e}")
            if driver: driver.quit()
            return None

        # --- Step 3: Click Submit Button ---
        try:
            print("Waiting for the submit button...")
            submit_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))
            )
            submit_button.click()
            print("Submit button clicked!")
            time.sleep(5)
            return driver
        except Exception as e:
            print(f"Submit button not found or not clickable: {e}")
            if driver: driver.quit()
            return None

    except Exception as e:
        print(f"An unexpected error occurred in the login module: {e}")
        if driver: driver.quit()
        return None