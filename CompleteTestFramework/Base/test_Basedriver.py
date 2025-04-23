import pytest
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import wait
from selenium.webdriver.support.expected_conditions import element_to_be_clickable
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


class BaseDriver:

    def __init__(self, driver):
        self.driver = driver

    def scroll_into_view(self,element):
        self.driver.execute_script("arguments[0].scrollIntoView(true);",element)

    def wait_until_clickable(self,element_type):
        wait = WebDriverWait(self.driver,10)
        wait.until(element_to_be_clickable(element_type)).click()

    def search_item1(self,locator_type,locator):
      return self.driver.find_element(locator_type,locator)