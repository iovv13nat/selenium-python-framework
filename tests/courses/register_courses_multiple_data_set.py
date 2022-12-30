import time

from pages.courses.register_courses_page import RegisterCoursesPage
from utilities.teststatus import TestStatus
import unittest
import pytest
from ddt import ddt, data, unpack


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
@ddt
class RegisterMultipleCoursesTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.courses = RegisterCoursesPage(self.driver)
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=1)
    @data(("JavaScript for beginners", "4120 5678 9012 3456", "1224", "321"),
          ("Selenium WebDriver Advanced", "4120 5678 9012 3456", "0324", "567"),
          ("Selenium WebDriver With Python 3.x", "4120 5678 9012 3456", "0925", "987"))
    @unpack
    def test_invalidEnrollment(self, courseName, ccNum, ccExp, ccCvc):
        self.courses.clickAllCoursesLink()
        self.courses.clickSearchBox()
        self.courses.enterCourseName(courseName)
        self.courses.selectCourseToEnroll(courseName)
        self.courses.enrollCourse(num=ccNum, exp=ccExp, cvc=ccCvc)
        result = self.courses.verifyEnrollFailed()
        self.ts.markFinal("test_invalidEnrollment", result, "Enrollment Failed Verification")



