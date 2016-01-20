# -*- coding: utf-8 -*-
"""Blog monitoring-fr.org"""

import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.expected_conditions import visibility_of
from selenium.webdriver.support.expected_conditions import presence_of_element_located

base_url = "http://www.monitoring-fr.org/"

driver = webdriver.Firefox()
wait = WebDriverWait(driver, 5)


class Suite(unittest.TestCase):
    """Test www page"""

    def test_01_openpage(self):
        """Open page"""
        driver.get(base_url)
        self.assertIn(u"Supervision, monitoring, métrologie, capacity planning à la sauce Open Source", driver.title)

    def test_02_solutions(self):
        """Open solutions page"""
        driver.find_element_by_link_text("Solutions").click()
        driver.find_element_by_link_text(u"Plus d’informations sur Shinken …").click()

        driver.find_element_by_xpath("//h1[text()='Shinken']")

    def test_03_search(self):
        """Test search box"""
        driver.find_element_by_id("s").clear()
        driver.find_element_by_id("s").send_keys("shinken",  Keys.ENTER)

        driver.find_element_by_link_text("Shinken")

    def test_04_admin_open(self):
        """Open admin panel"""
        driver.find_element_by_link_text("Connexion").click()
        driver.find_element_by_id("user_login")


if __name__ == "__main__":
    unittest.main(verbosity=2, exit=False)
    driver.quit()
