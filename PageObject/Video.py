import time
from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from utilities.utils import find_element, hover_over_action
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# I have added static time to Just to view the video
class Automation_video:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def mousetrapping(self):
        # Hover over to the video
        element = find_element(self.driver, By.CSS_SELECTOR, 'div[class="jw-controlbar jw-reset"]')
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()

    def Video(self):
        # Step 1: Sign in to the Platform
        find_element(self.driver, By.XPATH, "//input[@id='access-code']").send_keys("WVMVHWBS")
        find_element(self.driver, By.XPATH, "//span[contains(text(),'Sign In')]").click()

        # Step 2: Navigate to 'Test Automation Project'
        find_element(self.driver, By.XPATH, "//h5[contains(text(),'Test automation project')]").click()

        # Step 3: Switch to the 'Details' Tab
        find_element(self.driver, By.CSS_SELECTOR, 'a[aria-label="Details"]').click()

        # Step 4: Return to the 'Videos' Tab
        find_element(self.driver, By.CSS_SELECTOR, 'a[aria-label="Videos"]').click()
        time.sleep(2)

        # Step 5: Play the Video
        find_element(self.driver, By.CSS_SELECTOR, 'button[aria-label="Play Video"]').click()
        video_iframe = find_element(self.driver, By.CSS_SELECTOR, 'iframe[id="video_player"]')
        self.driver.switch_to.frame(video_iframe)

        self.mousetrapping()

        # Step 6: Pause the video when the timer reaches "00:10"
        Pause_button = find_element(self.driver, By.XPATH, '(//div[@aria-label="Pause"])[2]')
        while True:
            hover_over_action(self.driver, By.CSS_SELECTOR, 'div[class="jw-reset jw-button-container"]')
            try:
                timer = find_element(self.driver, By.XPATH, '(//div[@role="timer"])[1]')
                if timer.text == "00:10":
                    Pause_button.click()
                    time.sleep(2)
                    break
            except NoSuchElementException:
                print("Timer element not found.")
                break

        # Step 7: Replay the Video using 'Continue Watching' button
        self.driver.switch_to.default_content()
        find_element(self.driver, By.CSS_SELECTOR, 'button[aria-label="Continue Watching"]').click()
        self.driver.switch_to.frame(video_iframe)
        self.mousetrapping()

        # Step 8: Adjust Volume to 50%
        volume_button = find_element(self.driver, By.XPATH, '//div[@class="jw-reset jw-button-container"]/div[4]')
        actions = ActionChains(self.driver)
        actions.move_to_element(volume_button).perform()
        time.sleep(1)
        volume_slider = find_element(self.driver, By.CSS_SELECTOR,
                                     'div[aria-orientation="vertical"][aria-label="Volume"]')
        slider_height = volume_slider.size['height']
        total_offset = -slider_height / 2
        step = total_offset / 5
        actions.click_and_hold(volume_slider)
        actions.move_by_offset(0, step).perform()
        actions.release().perform()

        # Step 9: Change Video Resolution
        find_element(self.driver, By.CSS_SELECTOR, 'div[aria-label="Settings"]').click()
        time.sleep(5)  # Just to view the resolution changes
        find_element(self.driver, By.XPATH, '((//div[@id="jw-settings-menu"]/div)[2]/div/button)[3]').click()

        self.mousetrapping()

        find_element(self.driver, By.CSS_SELECTOR, 'div[aria-label="Settings"]').click()
        time.sleep(5)  # Just to view the resolution changes
        find_element(self.driver, By.XPATH, '((//div[@id="jw-settings-menu"]/div)[2]/div/button)[2]').click()

        find_element(self.driver, By.CSS_SELECTOR,
                     'div[aria-label="Settings"]').click()  # Just to view the updated resoltion
        time.sleep(5)  # Just to view the resolution changes

        # Step 10: Pause and Exit
        Pause_button.click()
        time.sleep(3)
        self.driver.switch_to.default_content()
        find_element(self.driver, By.CSS_SELECTOR, 'button[aria-label="Go Back and continue playing video"]').click()
        time.sleep(5)

        # Step 11: Sign Out
        wait = WebDriverWait(self.driver, 10)
        side_menu = wait.until(EC.presence_of_element_located((By.XPATH, "//aside[@id='SideBar']")))
        actions.move_to_element(side_menu).perform()
        sign_out_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@id='signOutSideBar']")))
        sign_out_button.click()
        time.sleep(2)
