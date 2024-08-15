from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from time import sleep
import os
from pathlib import Path
from selenium.webdriver.chrome.options import Options

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--headless")  # Note: `--headless` should be added to the same instance of options

# Set up Chrome driver using ChromeDriverManager
service = ChromeService(executable_path=ChromeDriverManager().install())

# Create a WebDriver object with the options
driver = webdriver.Chrome(service=service, options=chrome_options)

sleep(2)

# Open the web page
driver.get("https://login.yahoo.com/?.src=ym&pspid=159600001&activity=mail-direct&.lang=en-US&.intl=us&.done=https%3A%2F%2Fmail.yahoo.com%2Fd")

sleep(1)

# Scroll to the bottom of the page
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
sleep(2)

# Save a screenshot
current_path = Path(__file__).parent
screenshot_name = os.path.join(str(current_path), 'Section2.png')
driver.save_screenshot(screenshot_name)

# Close the browser
driver.quit()
