# -*- coding: utf-8 -*-
"""Wiki monitoring-fr.org"""
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.expected_conditions import visibility_of
from selenium.webdriver.support.expected_conditions import presence_of_element_located

base_url = "http://wiki.monitoring-fr.org/"

driver = webdriver.Firefox()
wait = WebDriverWait(driver, 5)


class Suite(unittest.TestCase):
    """Test wiki site"""

    def test_01_open_homepage(self):
        """Open homepage"""
        driver.get(base_url)
        self.assertIn(u"Accueil [wiki monitoring-fr.org]", driver.title)

    def test_02_eue(self):
        """Open eue page"""
        driver.find_element_by_link_text("Ressenti utilisateur avec sikuli").click()
        driver.find_element_by_xpath("//h1[text()='Supervision du ressenti utilisateur avec Sikuli']")

    def test_03_search(self):
        """Test search box"""
        driver.find_element_by_id("qsearch__in").clear()
        driver.find_element_by_id("qsearch__in").send_keys("icinga",  Keys.ENTER)
        driver.find_element_by_link_text("Présentation")

    def test_04_connexion_open(self):
        """Open connexion panel"""
        driver.find_element_by_link_text("S'identifier").click()
        driver.find_element_by_id("focus__this")

if __name__ == "__main__":
    unittest.main(verbosity=2, exit=False)
    driver.quit()
