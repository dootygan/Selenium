from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from time import sleep
Age = [12,12,23,18,45,17]
def myFunc(x):
    if x < 18:
        return False
    else:
        return True
adults = filter(myFunc, Age)
for x in adults:
    print(x)
beta_list = ['apple', 'banana', 'orange']
for x in range(1,2):
    beta_list += ["fruit"]
    print(beta_list)

class Car(object):
    """A simple Car class."""

    def __init__(self, color, doors, tires):
        """Constructor"""
        self.color = color
        self.doors = doors
        self.tires = tires

    def brake(self):
        """Stop the car"""
        return "Braking"

    def drive(self):
        """Drive the car"""
        return "I’m driving!"
def my_function():
    print("This function is being called.")

if __name__ == "__main__":
    print("This script is being run directly.")
    my_function()
