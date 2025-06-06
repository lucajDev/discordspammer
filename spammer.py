
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys

def spam_channel_with_message(driver, message_text, spam_count=None):
    if not message_text:
        print("No spam message was entered. Skipping spamming.")
        return
    DELAY_BETWEEN_MESSAGES = 1.5 # in seconds

    print(f"\nStarting to spam with the message: '{message_text}'")
    if spam_count is None:
        print(f"Sending messages every {DELAY_BETWEEN_MESSAGES}s (Press Ctrl+C in console to stop)...")
    else:
        print(f"Sending {spam_count} messages every {DELAY_BETWEEN_MESSAGES}s...")

    try:
        message_input_selector = "div[role='textbox']"
        message_input_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, message_input_selector))
        )

        sent_messages = 0
        while True:
            # Check if the driver window is still open before trying to send keys
            if not driver.window_handles:
                print("\nBrowser window was closed. Stopping spam.")
                break

            message_input_field.send_keys(message_text)
            message_input_field.send_keys(Keys.ENTER)
            sent_messages += 1
            print(f"Message {sent_messages} sent.")

            # IMPORTANT: Delay to avoid Discord rate limits!
            time.sleep(DELAY_BETWEEN_MESSAGES)

            if spam_count is not None and sent_messages >= spam_count:
                print(f"Target of {spam_count} messages reached.")
                break

    except KeyboardInterrupt:
        print("\nSpamming manually stopped (Ctrl+C).")
    except TimeoutException:
        print("Message input field not found. Stopping spam.")
    except Exception as e:
        print(f"An error occurred during spamming (the browser might have been closed): {e}")

    print("Spamming process finished.")