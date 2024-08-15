from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Specify the path to the ChromeDriver executable
service = Service(executable_path=r'C:\path\to\chromedriver.exe')

# Create a WebDriver instance with the Service object
driver = webdriver.Chrome(service=service)

# Open Google
driver.get("https://www.google.com/")
