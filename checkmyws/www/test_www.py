# -*- coding: utf-8 -*-
"""Checkmy.ws"""

import unittest

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

base_url = "https://checkmy.ws/"

driver = webdriver.Firefox()
wait = WebDriverWait(driver, 5)

class Suite(unittest.TestCase):
    """Check wooster website"""

def setUp(self):
  pass
  """les étapes du scenario viendront s'insérer ici"""

if __name__ == "__main__":
    unittest.main(verbosity=2, exit=False)
    driver.quit()
