import time

from selenium.webdriver.common.by import By
from base.selenium_driver import SeleniumDriver
import utilities.custom_logger as cl
import logging
from base.basepage import BasePage
from pages.home.navigation_page import NavigationPage


class LoginPage(BasePage):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.nav = NavigationPage(driver)

    #Locators
    _login_link = "//*[@id='navbar-inverse-collapse']/div/div"
    _email_field = "//input[@placeholder='Email Address']"
    _password_field = "//input[@placeholder='Password']"
    _login_button = "//input[@value='Login']"

    def clickLoginButton(self):
        self.elementClick(self._login_button, locatorType="xpath")


    def login(self, email="", password=""):
        self.clickLoginLink()
        # self.clearFields()
        self.enterEmail(email)
        self.enterPassword(password)

        self.clickLoginButton()

    def clickLoginLink(self,):
        self.elementClick(self._login_link, locatorType="xpath")

    def enterEmail(self, email):
        self.sendKeys(email, self._email_field, locatorType="xpath")

    def enterPassword(self, password):
        self.sendKeys(password, self._password_field, locatorType="xpath")



    def verifyLoginSuccessful(self):
        result = self.isElementPresent("//img[@class='zl-navbar-rhs-img ']",
                                       locatorType="xpath")
        return result


    def verifyLoginFailed(self):
        result = self.isElementPresent("//span[contains(text(),'Your username or password is invalid. Please try again.')]",
                                       locatorType="xpath")
        return result

    def verifyLoginTitle(self):
        return self.verifyPageTitle("My Courses")

    def logout(self):
        self.nav.navigateToUserIcon()
        logoutLinkElement = self.waitForElement(locator="//a[contains(text(),'Logout')]", locatorType="xpath", pollFrequency=1)
        self.elementClick(element = logoutLinkElement)




