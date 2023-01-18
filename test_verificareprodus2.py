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


class TestVerificareprodonline():
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_verificareprodus(self):
        # Test name: verificareprodus
        # Step # | name | target | value
        # 1 | open | /en/ |
        self.driver.get("http://34.118.122.203/en/")
        # 2 | setWindowSize | 1900x1020 |
        self.driver.set_window_size(1900, 1020)
        # 3 | click | css=a > .hidden-sm-down |
        self.driver.find_element(By.CSS_SELECTOR, "a > .hidden-sm-down").click()
        # 4 | click | id=field-email |
        self.driver.find_element(By.ID, "field-email").click()
        # 5 | type | id=field-email | maricaandrei60@gmail.com
        self.driver.find_element(By.ID, "field-email").send_keys("maricaandrei60@gmail.com")
        # 6 | click | id=field-password |
        self.driver.find_element(By.ID, "field-password").click()
        # 6 | type | id=field-password | octopussy581A
        self.driver.find_element(By.ID, "field-password").send_keys("octopussy581A")
        # 8 | click | id=submit-login |
        self.driver.find_element(By.ID, "submit-login").click()
        # 9 | click | css=.logo |
        self.driver.find_element(By.CSS_SELECTOR, ".logo").click()
        # 10 | click | css=.featured-products:nth-child(2) .js-product:nth-child(7) img |
        self.driver.find_element(By.CSS_SELECTOR, ".featured-products:nth-child(2) .js-product:nth-child(7) img").click()
        # 11 | click | css=.js-product-flags > .online-only |
        self.driver.implicitly_wait(3)
        self.driver.find_element(By.CSS_SELECTOR, ".js-product-flags > .online-only").click()
        # 12 | click | css=.add-to-cart |
        self.driver.find_element(By.CSS_SELECTOR, ".add-to-cart").click()
        # 13 | click | css=.btn > .rtl-no-flip |
        # self.driver.find_element(By.CSS_SELECTOR, ".btn > .rtl-no-flip").click()
        produsverificat = WebDriverWait(self.driver, 15).until(
            lambda d: d.find_element(By.CSS_SELECTOR, ".btn > .rtl-no-flip"))
        produsverificat.click()
        # 14 | click | css=.text-sm-center > .btn |
        self.driver.find_element(By.CSS_SELECTOR, ".text-sm-center > .btn").click()
        # 15 | click | linkText=add new address |
        self.driver.find_element(By.LINK_TEXT, "add new address").click()
        # 16 | click | id=field-address1 |
        self.driver.find_element(By.ID, "field-address1").click()
        # 17 | type | id=field-address1 | emil racovita
        self.driver.find_element(By.ID, "field-address1").send_keys("emil racovita")
        # 18 | click | id=field-city |
        self.driver.find_element(By.ID, "field-city").click()
        # 19 | type | id=field-city | Brasov
        self.driver.find_element(By.ID, "field-city").send_keys("Brasov")
        # 20 | click | id=field-id_state |
        self.driver.find_element(By.ID, "field-id_state").click()
        # 21 | select | id=field-id_state | label=AA
        dropdown = self.driver.find_element(By.ID, "field-id_state")
        dropdown.find_element(By.XPATH, "//option[. = 'AA']").click()
        # 22 | click | id=field-postcode |
        self.driver.find_element(By.ID, "field-postcode").click()
        # 23 | type | id=field-postcode | 50011
        self.driver.find_element(By.ID, "field-postcode").send_keys("50011")
        # 24 | click | name=confirm-addresses |
        self.driver.find_element(By.NAME, "confirm-addresses").click()
        # 25 | click | name=confirmDeliveryOption |
        self.driver.find_element(By.NAME, "confirmDeliveryOption").click()
        # 26 | click | id=payment-option-3 |
        self.driver.find_element(By.ID, "payment-option-3").click()
        # 27 | click | id=conditions_to_approve[terms-and-conditions] |
        self.driver.find_element(By.ID, "conditions_to_approve[terms-and-conditions]").click()
        # 28 | click | css=.ps-shown-by-js > .btn |
        self.driver.find_element(By.CSS_SELECTOR, ".ps-shown-by-js > .btn").click()
        assert 'online-only' in self.driver.page_source
