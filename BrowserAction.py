from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from time import sleep

# Set up the Chrome driver
service = ChromeService(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
sleep(2)

# Open Google
driver.get('https://www.google.com/')

# Get and print the title of the page
window_title = driver.title
print(f"Window title: {window_title}")

# Find the search box, enter "wikipedia", and press Enter
search_box = driver.find_element('name', 'q')
search_box.send_keys("wikipedia")
search_box.send_keys(Keys.RETURN)
sleep(1)

# Navigate back, forward, and refresh the page
driver.back()
sleep(1)
driver.forward()
sleep(1)
driver.refresh()
sleep(1)

# Open a new tab and navigate to Gmail
driver.switch_to.new_window('tab')
driver.get('https://gmail.com/')
sleep(1)

# Open a new window and navigate to Yahoo login
driver.switch_to.new_window('window')
driver.get('https://login.yahoo.com/')
sleep(1)

# Get and print the current Yahoo window handle
yahoo_window = driver.current_window_handle
print(f"Yahoo window handle: {yahoo_window}")

# Get the size of the window
window_size = driver.get_window_size()
print(f"Window size: {window_size}")

# Set window size to 800x600
driver.set_window_size(800, 600)
new_size = driver.get_window_size()
assert new_size['width'] == 800, f"Expected width 800 but got {new_size['width']}"
assert new_size['height'] == 600, f"Expected height 600 but got {new_size['height']}"
driver.fullscreen_window()