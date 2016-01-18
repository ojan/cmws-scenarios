# -*- coding: utf-8 -*-
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

    def test_05_admin_login(self):
        """Login on admin panel"""
        user_login = driver.find_element_by_id("user_login")
        user_pass = driver.find_element_by_id("user_pass")

        user_login.clear()
        user_login.send_keys("test@monitoring-fr")

        user_pass.clear()
        user_pass.send_keys("nagios")

        wait.until(
            lambda driver: user_pass.get_attribute("value") != "",
            message="Field 'user_pass' not filled"
        )

        driver.find_element_by_id("wp-submit").click()

        driver.find_element_by_id("adminmenu")

    def test_06_admin_dashboard(self):
        """Open dashboard"""
        driver.find_element_by_css_selector("#menu-dashboard > a").click()
        driver.find_element_by_id("dashboard-widgets-wrap")

    def test_07_admin_logout(self):
        """Logout"""
        menu = driver.find_element_by_id("wp-admin-bar-my-account")
        submenu = driver.find_element_by_css_selector("#wp-admin-bar-logout .ab-item")

        # Move cursor on menu
        ActionChains(driver).move_to_element(menu).perform()
        wait.until(visibility_of(submenu))

        # Click on submenu
        submenu.click()

        wait.until(presence_of_element_located((By.ID, "user_login")))

    def test_08_admin_backtohome(self):
        """Back to homepage"""
        driver.find_element_by_link_text(u"← Retour sur Communauté Francophone de la Supervision Libre").click()
        driver.find_element_by_link_text("Wiki")


if __name__ == "__main__":
    unittest.main(verbosity=2, exit=False)
    driver.quit()
