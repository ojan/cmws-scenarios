# -*- coding: utf-8 -*-
"""Wooster Checkmy.ws"""

import unittest
from os import environ

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

base_url = "https://wooster.checkmy.ws/"
base_url = environ.get("URL", base_url)

driver = webdriver.Firefox()
wait = WebDriverWait(driver, 5)

class Suite(unittest.TestCase):
    """Test wooster Website"""

    def test_01_home(self):
        """Get Home page"""
        driver.get(base_url)
        self.assertIn(u"Supervision & performance des sites web. - Wooster", driver.title)

    def test_02_archives(self):
        """Get Archives page"""
        driver.find_element_by_link_text("ARCHIVES").click()
        driver.find_element_by_xpath("//h1[text()='Archives Wooster']")

    def test_03_doc(self):
        """Get Doc page"""
        driver.find_element_by_link_text("DOC").click()
        driver.find_element_by_xpath("//h1[text()='Howtos, guides, didacticiels']")

    def test_04_about(self):
        """Get À Propos page"""
        driver.find_element_by_link_text("À PROPOS").click()
        driver.find_element_by_xpath("//h1[text()='À propos de Wooster']")

if __name__ == "__main__":
    unittest.main(verbosity=2, exit=False)
    driver.quit()
