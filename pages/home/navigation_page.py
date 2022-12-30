import time

from selenium.webdriver.common.by import By
from base.selenium_driver import SeleniumDriver
import utilities.custom_logger as cl
import logging
from base.basepage import BasePage


class NavigationPage(BasePage):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #Locators
    _home = "//a[contains(text(),'HOME')]"
    _all_courses = "//div[@id='navbar-inverse-collapse']//a[@href='/courses']"
    _support = "//a[contains(text(),'SUPPORT')]"
    _my_courses = "//a[contains(text(),'MY COURSES')]"
    _user_icon = "//img[@class='zl-navbar-rhs-img ']"

    def navigateToAllCourses(self):
        self.elementClick(locator=self._all_courses, locatorType='xpath')

    def navigateToHome(self):
        self.elementClick(locator=self._home, locatorType='xpath')

    def navigateToSupport(self):
        self.elementClick(locator=self._support, locatorType='xpath')

    def navigateToMyCourses(self):
        self.elementClick(locator=self._my_courses, locatorType='xpath')

    def navigateToUserIcon(self):
        userIconElement = self.waitForElement(locator=self._user_icon, locatorType='xpath', pollFrequency=1)
        self.elementClick(element=userIconElement)



