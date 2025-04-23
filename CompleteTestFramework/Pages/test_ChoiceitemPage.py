
from selenium.webdriver.common.by import By
from selenium.webdriver.support import wait
from selenium import webdriver

from Base.test_Basedriver import BaseDriver

class ChooseItem(BaseDriver):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver


#Externalise the locators
    CHOICE = "//img[@alt='Coffee Cup Espresso Cup Mug Set of 6 Double Wall Stainless Steel Tea Cups,Reuse']"


    def choice_item_scroll(self):
        choice = self.search_item1(By.XPATH, self.CHOICE)
        self.scroll_into_view(choice)
        self.wait_until_clickable(choice)




