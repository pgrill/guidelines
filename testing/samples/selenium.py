from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from unittest import TestCase

class UserActivitiesTest(TestCase):
    def setUp(self):
        # (...) test setup, creating user and context

        # First we load the selenium driver, its responsable of controlling
        # the browser.
        # We like using a chrome webdriver as its our goto browser
        self.selenium = webdriver.Chrome(<path_to_driver>)
        self.selenium.maximize_window()
        super().setUp()

    def tearDown(self):
        # Its important to close the selenium session
        # once out test are done
        self.selenium.quit()
        super().tearDown()

    def test_async_user_activities(self):
        # Load the page into the browser
        self.selenium.get(
            '{}{}'.format(self.live_server_url, '/user/1/activities')
        )

        # We can select DOM elements and interact with them
        activity_button = self.selenium.find_element_by_id("activity-button")
        activity_button.click()

        # We wait for the activities maximum (acceptable) time
        # and set the expected condition, if the time is reached and
        # the condition evaluates to false, the test will fail.
        WebDriverWait(self.selenium, 10).until(
            expected_conditions.visibility_of_element_located(
                (By.CLASS_NAME, "user-activity")
            )
        )
