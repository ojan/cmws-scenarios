# -*- coding: utf-8 -*-
"""Doc monitoring-fr.org"""

import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.expected_conditions import visibility_of
from selenium.webdriver.support.expected_conditions import presence_of_element_located

base_url = "http://doc.monitoring-fr.org/"

driver = webdriver.Firefox()
wait = WebDriverWait(driver, 5)


class Suite(unittest.TestCase):
    """Test doc page"""

    def test_01_openpage(self):
        """Open page"""
        driver.get(base_url)
        self.assertIn(u"Traduction Documentation Officielle Nagios | monitoring-fr.org", driver.title)

    def test_02_solutions(self):
        """Open solutions page"""
        driver.find_element_by_link_text(u"Nagios Version 3.x HTML [fr_FR]").click()
        driver.find_element_by_xpath("//h1[text()='Documentation Nagios Version 3.x']")

    def test_03_solutions(self):
        """Open solutions page"""
        driver.find_element_by_link_text("Suivant").click()
        driver.find_element_by_xpath("//h1[text()='Partie I. À propos']")

    def test_04_solutions(self):
        """Open solutions page"""
        driver.find_element_by_link_text("Sommaire").click()
        driver.find_element_by_xpath("//h1[text()='Documentation Nagios Version 3.x']")

    def test_05_solutions(self):
        """Open solutions page"""
        driver.find_element_by_link_text("Glossaire").click()
        driver.find_element_by_xpath("//h2[text()='Glossaire']")

if __name__ == "__main__":
    unittest.main(verbosity=2, exit=False)
    driver.quit()
