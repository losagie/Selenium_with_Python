import pytest
from selenium import webdriver
from selenium.webdriver.common.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

#Construct the set-up and tear down method
@pytest.fixture(scope="class")
def setup_meth(request,browser,url):

        if browser == "chrome":
                driver = webdriver.Chrome()
        elif browser == "edge":
                driver = webdriver.Edge()
        else:
                driver = webdriver.Firefox()
        driver.get(url)
        driver.maximize_window()
        request.cls.driver = driver
        #request.cls.wait = wait
        yield
        driver.quit()


#Add browser and url options
def pytest_addoption(parser):
        parser.addoption("--browser", default="chrome")
        parser.addoption("--url")

@pytest.fixture(scope="class", autouse=True)
def browser(request):
      return  request.config.getoption("--browser")

@pytest.fixture(scope="class", autouse=True)
def url(request):
      return  request.config.getoption("--url")


