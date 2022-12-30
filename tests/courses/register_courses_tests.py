import time

from pages.courses.register_courses_page import RegisterCoursesPage
from utilities.teststatus import TestStatus
import unittest
import pytest


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class RegisterCoursesTests(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.courses = RegisterCoursesPage(self.driver)
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=1)
    def test_invalidEnrollment(self):
        # self.courses.clickAllCoursesLink()
        # self.courses.clickSearchBox()
        #self.courses.clickSubmitButton()
        self.courses.enterCourseName("JavaScript")
        self.courses.selectCourseToEnroll("JavaScript for beginners")
        self.courses.enrollCourse(num="4120 5678 9012 3456", exp="1224", cvc="231")
        result = self.courses.verifyEnrollFailed()
        self.ts.markFinal("test_invalidEnrollment", result, "Enrollment Failed Verification")

