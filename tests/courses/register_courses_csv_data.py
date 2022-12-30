import time

from selenium.webdriver.common.by import By
from pages.home.navigation_page import NavigationPage
from pages.courses.register_courses_page import RegisterCoursesPage
from utilities.teststatus import TestStatus
import unittest
import pytest
from ddt import ddt, data, unpack
from utilities.read_data import getCSVData


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
@ddt
class RegisterCoursesCSVDataTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.courses = RegisterCoursesPage(self.driver)
        self.ts = TestStatus(self.driver)
        self.nav = NavigationPage(self.driver)

    def setUp(self):
        self.nav.navigateToAllCourses()
    @pytest.mark.run(order=1)
    @data(*getCSVData("/Users/nataliakeegan/workspace_python/letskodeit/testdata.csv"))
    @unpack
    def test_invalidEnrollment(self, courseName, ccNum, ccExp, ccCvc):
        # self.courses.clickAllCoursesLink()
        self.courses.clickSearchBox()
        self.courses.enterCourseName(courseName)
        self.courses.selectCourseToEnroll(courseName)
        self.courses.enrollCourse(num=ccNum, exp=ccExp, cvc=ccCvc)
        result = self.courses.verifyEnrollFailed()
        self.ts.markFinal("test_invalidEnrollment", result, "Enrollment Failed Verification")



