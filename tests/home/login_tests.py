import pytest
from utilities.teststatus import TestStatus
from pages.home.login_page import LoginPage
import unittest

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class LoginTests(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)
        self.ts = TestStatus(self.driver)

    #Need to verify two verifications points
    #1 fails, code will not go to the next verification point
    #If assert fails , it stops current test execution and moves to the next test method
    @pytest.mark.run(order=2)
    def test_validLogin(self):
        self.lp.login("iovv13@mail.ru", "abcabc")
        result1 = self.lp.verifyLoginTitle()
        self.ts.mark(result1, "Title Verification")
        result2 = self.lp.verifyLoginSuccessful()
        self.ts.markFinal("test_validLogin", result2, "Login was  successful")



    @pytest.mark.run(order=1)
    def test_invalidLogin(self):
        self.lp.logout()
        self.lp.login("iovv13@mail.ru", "abcabckkk")
        result = self.lp.verifyLoginFailed()
        assert result == True





