
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

def get_id_from_console(prompt_message):
    user_input = input(prompt_message).strip()
    return user_input

def click_div_with_data_list_item_id(driver, server_id):

    if not server_id:
        print("Server ID was not entered. Skipping server click.")
        return False

    try:
        print(f"Waiting for the DIV with Server ID '{server_id}'...")
        server_div_selector = f"div[data-list-item-id='guildsnav___{server_id}']"

        server_element = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, server_div_selector))
        )
        server_element.click()
        print(f"Clicked the DIV with Server ID '{server_id}'!")
        time.sleep(5)  # Pause to allow the server to load
        return True
    except TimeoutException:
        print(f"DIV with Server ID '{server_id}' was not found within the timeout period.")
        return False
    except Exception as e:
        print(f"An error occurred while finding the DIV with Server ID '{server_id}': {e}")
        return False

def click_channel_by_id(driver, channel_id):
    if not channel_id:
        print("Channel ID was not entered. Skipping channel click.")
        return False

    try:
        print(f"Waiting for the channel with ID '{channel_id}'...")
        # CSS selector: a[data-list-item-id='channels___CHANNELID']
        channel_element_selector = f"a[data-list-item-id='channels___{channel_id}']"

        channel_element = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, channel_element_selector))
        )
        channel_element.click()
        print(f"Clicked the channel with ID '{channel_id}'!")
        time.sleep(3)
        return True
    except TimeoutException:
        print(f"Channel with ID '{channel_id}' not found within the timeout period.")
        return False
    except Exception as e:
        print(f"An error occurred while finding the channel A-TAG with ID '{channel_id}': {e}")
        return False