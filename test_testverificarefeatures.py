# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestTestverificarefeatures():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_testverificarefeatures(self):
    # Test name: test verificare features
    # Step # | name | target | value
    # 1 | open | /ro/ | 
    self.driver.get("http://34.118.122.203/ro/")
    # 2 | setWindowSize | 1900x1020 | 
    self.driver.set_window_size(1900, 1020)
    # 3 | click | css=a > .hidden-sm-down | 
    self.driver.find_element(By.CSS_SELECTOR, "a > .hidden-sm-down").click()
    # 4 | click | id=field-email | 
    self.driver.find_element(By.ID, "field-email").click()
    # 5 | type | id=field-email | maricaandrei60@gmail.com
    self.driver.find_element(By.ID, "field-email").send_keys("maricaandrei60@gmail.com")
    # 6 | type | id=field-password | octopussy581A
    self.driver.find_element(By.ID, "field-password").send_keys("octopussy581A")
    # 7 | click | css=.form-group:nth-child(3) | 
    self.driver.find_element(By.CSS_SELECTOR, ".form-group:nth-child(3)").click()
    # 8 | click | id=submit-login | 
    self.driver.find_element(By.ID, "submit-login").click()
    # 9 | click | css=#category-4 > .dropdown-item |
    self.driver.implicitly_wait(3)
    self.driver.find_element(By.CSS_SELECTOR, "#category-3 > .dropdown-item").click()
    # 10 | click | css=.js-product:nth-child(2) img | 
    self.driver.find_element(By.CSS_SELECTOR, ".js-product:nth-child(2) img").click()
    # 11 | click | css=.data-sheet | 
    self.driver.find_element(By.CSS_SELECTOR, ".data-sheet").click()
    # 12 | click | css=.tabs | 
    self.driver.find_element(By.CSS_SELECTOR, ".tabs").click()
    # 13 | click | css=.add-to-cart | 
    self.driver.find_element(By.CSS_SELECTOR, ".add-to-cart").click()
    # 14 | click | css=.cart-content-btn > .btn-secondary | 
    self.driver.find_element(By.CSS_SELECTOR, ".cart-content-btn > .btn-secondary").click()
    # 15 | click | css=.product-accessories .js-product:nth-child(2) img | 
    self.driver.find_element(By.CSS_SELECTOR, ".product-accessories .js-product:nth-child(2) img").click()
    # 16 | click | css=.data-sheet | 
    self.driver.find_element(By.CSS_SELECTOR, ".data-sheet").click()
    # 17 | click | css=.product-accessories > .products | 
    self.driver.find_element(By.CSS_SELECTOR, ".product-accessories > .products").click()
    # 18 | click | css=.add-to-cart | 
    self.driver.find_element(By.CSS_SELECTOR, ".add-to-cart").click()
    # 19 | click | css=.cart-content-btn > .btn-secondary | 
    self.driver.find_element(By.CSS_SELECTOR, ".cart-content-btn > .btn-secondary").click()
    # 20 | click | css=#category-10 > .dropdown-item |
    self.driver.implicitly_wait(3)
    self.driver.find_element(By.CSS_SELECTOR, "#category-10 > .dropdown-item").click()
    # 21 | click | css=.js-product:nth-child(4) img | 
    self.driver.find_element(By.CSS_SELECTOR, ".js-product:nth-child(4) img").click()
    # 22 | click | css=.data-sheet | 
    self.driver.find_element(By.CSS_SELECTOR, ".data-sheet").click()
    self.driver.find_element(By.CSS_SELECTOR, ".product-accessories > .products").click()
    # 23 | click | css=.tabs | 
    self.driver.find_element(By.CSS_SELECTOR, ".tabs").click()
    # 24 | click | css=.add-to-cart |
    self.driver.find_element(By.CSS_SELECTOR, ".add-to-cart").click()
    # 25 | click | css=.cart-content-btn > .btn-secondary | 
    self.driver.find_element(By.CSS_SELECTOR, "#category-10 > .dropdown-item").click()
    # 26 | click | css=.product-accessories img |
    self.driver.find_element(By.CSS_SELECTOR, ".js-product:nth-child(4) img").click()
    self.driver.find_element(By.CSS_SELECTOR, ".product-accessories img").click()
    # 27 | click | css=.data-sheet | 
    self.driver.find_element(By.CSS_SELECTOR, ".data-sheet").click()
    self.driver.find_element(By.CSS_SELECTOR, ".product-accessories > .products").click()
    # 28 | click | css=.tabs | 
    self.driver.find_element(By.CSS_SELECTOR, ".tabs").click()
    # 29 | click | css=.add-to-cart |
    self.driver.find_element(By.CSS_SELECTOR, ".add-to-cart").click()
    # 30 | click | css=.cart-content-btn > .btn-secondary | 
    self.driver.find_element(By.CSS_SELECTOR, ".cart-content-btn > .btn-secondary").click()
    # 31 | click | css=#category-16 > .dropdown-item | 
    self.driver.find_element(By.CSS_SELECTOR, "#category-16 > .dropdown-item").click()
    # 32 | click | css=.js-product:nth-child(1) img | 
    self.driver.find_element(By.CSS_SELECTOR, ".js-product:nth-child(1) img").click()
    # 33 | click | id=product-details | 
    self.driver.find_element(By.ID, "product-details").click()
    # 34 | click | id=product-details | 
    self.driver.find_element(By.ID, "product-details").click()
    # 35 | click | css=.add-to-cart | 
    self.driver.find_element(By.CSS_SELECTOR, ".add-to-cart").click()
    # 36 | click | css=.cart-content-btn > .btn-secondary | 
    self.driver.find_element(By.CSS_SELECTOR, ".cart-content-btn > .btn-secondary").click()
    # 37 | click | css=.product-accessories .js-product:nth-child(2) img | 
    self.driver.find_element(By.CSS_SELECTOR, ".product-accessories .js-product:nth-child(2) img").click()
    # 38 | click | css=.data-sheet | 
    self.driver.find_element(By.CSS_SELECTOR, ".data-sheet").click()
    # 39 | click | css=.value | 
    self.driver.find_element(By.CSS_SELECTOR, ".value").click()
    # 40 | click | css=.add-to-cart | 
    self.driver.find_element(By.CSS_SELECTOR, ".add-to-cart").click()
    # 41 | click | css=.cart-content-btn > .btn-secondary | 
    self.driver.find_element(By.CSS_SELECTOR, ".cart-content-btn > .btn-secondary").click()
    # # 42 | click | css=#category-15 > .dropdown-item |
    # self.driver.find_element(By.CSS_SELECTOR, "#category-15 > .dropdown-item").click()
    # # 43 | click | css=.js-product:nth-child(1) img |
    # self.driver.find_element(By.CSS_SELECTOR, ".js-product:nth-child(1) img").click()
    # # 44 | click | css=.add-to-cart |
    # self.driver.find_element(By.CSS_SELECTOR, ".add-to-cart").click()
    # # 45 | click | css=.cart-content-btn > .btn-primary |
    # self.driver.find_element(By.CSS_SELECTOR, ".cart-content-btn > .btn-primary").click()
    # self.driver.find_element(By.CSS_SELECTOR, "a:nth-child(1) > .hidden-sm-down").click()
    pagina = self.driver.find_element(By.ID, "main")
    prezentare_produs = pagina.find_element(By.XPATH, "/html/body/main/section/div/div/section/div[1]")
    coloana_detalii = prezentare_produs.find_element(By.XPATH, "/html/body/main/section/div/div/section/div[1]/div[2]")
    informatii_produs = coloana_detalii.find_element(By.CLASS_NAME, "product-information")
    taburi = informatii_produs.find_element(By.CLASS_NAME, "tabs")
    continut_tab = taburi.find_element(By.CLASS_NAME, "tab-content")
    afis = continut_tab.find_element(By.ID, "product-details")
    caracteristici = afis.find_element(By.CLASS_NAME, "product-features")
    detalii = caracteristici.find_element(By.CLASS_NAME, "data-sheet")
    assert detalii



    # 46 | click | css=.text-sm-center > .btn | 
    # self.driver.find_element(By.CSS_SELECTOR, ".text-sm-center > .btn").click()
    # # 47 | click | name=confirm-addresses |
    # self.driver.find_element(By.NAME, "confirm-addresses").click()
    # # 48 | click | name=confirmDeliveryOption |
    # self.driver.find_element(By.NAME, "confirmDeliveryOption").click()
    # # 49 | click | id=conditions_to_approve[terms-and-conditions] |
    # self.driver.find_element(By.ID, "conditions_to_approve[terms-and-conditions]").click()
    # # 50 | click | css=.ps-shown-by-js > .btn |
    # self.driver.find_element(By.CSS_SELECTOR, ".ps-shown-by-js > .btn").click()

  
