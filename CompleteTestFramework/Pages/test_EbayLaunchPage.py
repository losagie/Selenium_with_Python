from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from Base.test_Basedriver import BaseDriver


class Search_Item(BaseDriver):  #Search Item Class

    def __init__(self,driver):
        self.driver = driver
        super().__init__(driver)
        #self.wait = wait

    #Extenalize the Locators
    SEARCH_ITEM = "//input[@id='gh-ac']"
    SEARCH_CLICKS = "//span[@class='gh-search-button__label']"
    CONTROL_A = "//input[@id='gh-ac']"
    CATEGORIES = "//select[@id='gh-cat']"
    SEARCH_CLASS = "gh-search-button__label"


    def search_item(self):
        return self.search_item1(By.XPATH, self.SEARCH_ITEM)

    def search_items(self,item):
        self.search_item().send_keys(item)

    def search_click(self):
        return self.search_item1(By.XPATH,self.SEARCH_CLICKS)

    def search_clicks(self):
        self.search_click().click()

    def remove_text(self):
        return self.search_item1(By.XPATH, self.CONTROL_A)

    def remove_text1(self):
       self.remove_text().send_keys(Keys.CONTROL + "a")
       self.remove_text().send_keys(Keys.DELETE)


    def choose_categories(self,item_index):
        #self.driver.find_element(By.XPATH,"//select[@id='gh-cat']")
        categories = self.search_item1(By.XPATH,self.CATEGORIES)
        select = Select(categories)
        select.select_by_index(item_index)
        search = self.search_item1(By.CLASS_NAME,self.SEARCH_CLASS)
        search.click()