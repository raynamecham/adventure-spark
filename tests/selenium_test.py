import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class AdventureSparkTestCase(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()

    def testPageTitle(self):
        self.browser.maximize_window()
        self.browser.get('http://localhost:5000/')
        self.assertIn('Adventure Spark', self.browser.title)

    def testLogIn(self):
        self.browser.maximize_window()
        self.browser.get('http://localhost:5000/')

        elem = self.browser.find_element(By.ID, 'login')
        elem.click()
        email = self.browser.find_element(By.ID, 'login-email')
        email.send_keys('admin@admin.com')
        password = self.browser.find_element(By.ID, 'login-password')
        password.send_keys('password' + Keys.RETURN)

    def tearDown(self):
        self. browser.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)