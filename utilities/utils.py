import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.webdriver import WebDriver

# helper functions

def hover_over_action(driver: WebDriver, by: By, selector: str, timeout: int =100):
    try:
        element = WebDriverWait(driver, timeout).until(
            EC.visibility_of_element_located((by, selector ))
        )
        actions = ActionChains(driver)
        actions.move_to_element(element).perform()

    except Exception as e:
        print(f"An error occurred: {e}")


def find_element(driver: WebDriver, by: By, selector: str, timeout: int = 100):
    wait = WebDriverWait(driver, timeout)
    elements = wait.until(EC.visibility_of_element_located((by, selector)))
    return elements
