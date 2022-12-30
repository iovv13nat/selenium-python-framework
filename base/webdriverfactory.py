"""
@package base

WebDriver Factory class implementation
It creates a webdriver instance based on browser configurations

example:
 wdf = WebDriverFactory(browser)
 wdf.getWebDriverInstance()
"""
import os
import traceback
from selenium import webdriver

class WebDriverfactory():

    def __init__(self, browser):
        """
        Inits WebDriverFactory class
        Returns
           None
        :param browser:

        """
        self.browser = browser
        """
        Set chrome driver and iexploree environment based on OS
        chromedriver = "C:/.../chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = chromedriver
        self.driver = webdriver.Chrome(chromedriver)
        """

    def getWebDriverInstance(self):
        baseURL = "https://courses.letskodeit.com/"
        if self.browser == "iexplorer":
            #Set ie driver
            driver = webdriver.Ie()
        elif self.browser == "firefox":
            driver = webdriver.Firefox()
        elif self.browser == "chrome":
            #Set chrome driver
            chromedriver = "/Users/nataliakeegan/workspace_python/drivers/chromedriver"
            os.environ["webdriver.chrome.driver"] = chromedriver
            driver = webdriver.Chrome(chromedriver)
            driver.set_window_size(2560, 1600)
        else:
            driver = webdriver.Firefox()
        driver.implicitly_wait(3)
        driver.maximize_window()
        driver.get(baseURL)
        return driver
