import utilities.custom_logger as cl
import logging
from base.basepage import BasePage
class RegisterCoursesPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #Locators
    # _all_courses_link = "//div[@id='navbar-inverse-collapse']//a[@href='/courses']"
    _search_box = "//input[@id='search']"
    _submit_button = "//*[@class='find-course search-course']"
    _course = "//h4[contains(@class,'dynamic-heading') and contains(text(),'{0}')]"
    _enroll_button = "//button[contains(text(),'Enroll in Course')]"
    _cc_number = "//input[@placeholder='Card Number']"
    _cc_exp = "//input[@name='exp-date']"
    _cc_cvc = "//input[@placeholder='Security Code']"

    _submit_enroll = "//*[@id='checkout-form']/div[2]/div[3]/div/div[1]/div[2]/div/button[1]"
    _error_message = "//span[contains(text(),'Your card number is incomplete.')]"

    # def clickAllCoursesLink(self):
    #     self.elementClick(locator=self._all_courses_link, locatorType='xpath')

    def clickSearchBox(self):
        self.elementClick(locator=self._search_box, locatorType="xpath")

    def enterCourseName(self, name):
        self.sendKeys(name, locator=self._search_box, locatorType="xpath")
        self.elementClick(locator=self._submit_button, locatorType="xpath")

    # def clickSubmitButton(self):
    #     self.elementClick(locator=self._submit_button, locatorType='xpath')

    def selectCourseToEnroll(self, fullCourseName):
        self.elementClick(locator=self._course.format(fullCourseName), locatorType="xpath")

    def clickOnEnrolllButton(self):
        self.elementClick(locator=self._enroll_button, locatorType='xpath')

    def enterCardNum(self, num):
        self.SwitchFrameByIndex(self._cc_number, locatorType="xpath")
        self.sendKeysWhenReady(num, locator=self._cc_number, locatorType="xpath")
        self.switchToDefaultContent()

    def enterCardExp(self, exp):
        #self.switchToFrame(index=0)
        self.SwitchFrameByIndex(self._cc_exp, locatorType="xpath")
        self.sendKeys(exp, locator=self._cc_exp, locatorType="xpath")
        self.switchToDefaultContent()

    def enterCardCVC(self, cvc):
        self.SwitchFrameByIndex(self._cc_cvc, locatorType="xpath")
        self.sendKeys(cvc, locator=self._cc_cvc, locatorType="xpath")
        self.switchToDefaultContent()

    def clickEnrollSubmitButton(self):
        self.elementClick(locator=self._submit_enroll, locatorType="xpath")

    def enterCreditCardInformation(self, num, exp, cvc):
        self.enterCardNum(num)
        self.enterCardExp(exp)
        self.enterCardCVC(cvc)

    def enrollCourse(self, num="", exp="", cvc=""):
        # self.clickAllCoursesLink()
        # self.enterCourseName("JavaScript")
        # self.clickSubmitButton()
        self.clickOnEnrolllButton()
        self.webScroll(direction="down")
        self.enterCreditCardInformation(num, exp, cvc)
        self.clickEnrollSubmitButton()

    def verifyEnrollFailed(self):
        result = self.isEnabled(locator=self._submit_enroll, locatorType="xpath", info="Buy Button")
        return not result

