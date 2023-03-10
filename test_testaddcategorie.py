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

class TestTestaddcategorie():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_testaddcategorie(self):
    # Test name: test add categorie
    # Step # | name | target | value
    # 1 | open | http://34.118.122.203/administration/index.php?controller=AdminLogin&logout=1&token=958fb60fa7caa6709f45c58954e32439 | 
    self.driver.get("http://34.118.122.203/administration/index.php?controller=AdminLogin&logout=1&token=958fb60fa7caa6709f45c58954e32439")
    # 2 | setWindowSize | 1920x1040 | 
    self.driver.set_window_size(1920, 1040)
    # 3 | click | id=email | 
    self.driver.find_element(By.ID, "email").click()
    # 4 | type | id=email | maricaandrei60@gmail.com
    self.driver.find_element(By.ID, "email").send_keys("maricaandrei60@gmail.com")
    # 5 | type | id=passwd | 123456789
    self.driver.find_element(By.ID, "passwd").send_keys("123456789")
    # 6 | click | id=submit_login | 
    self.driver.find_element(By.ID, "submit_login").click()
    # 7 | mouseOver | id=submit_login | 
    element = self.driver.find_element(By.ID, "submit_login")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    # 8 | click | css=#subtab-AdminCatalog > .link |
    self.driver.implicitly_wait(3)
    self.driver.find_element(By.CSS_SELECTOR, "#subtab-AdminCatalog > .link").click()
    # 9 | click | linkText=Categories | 
    self.driver.find_element(By.LINK_TEXT, "Categories").click()
    # 10 | click | id=page-header-desc-configuration-add | 
    self.driver.find_element(By.ID, "page-header-desc-configuration-add").click()
    # 11 | click | id=category_name_1 | 
    self.driver.find_element(By.ID, "category_name_1").click()
    # 12 | type | id=category_name_1 | test add admin
    self.driver.find_element(By.ID, "category_name_1").send_keys("test add admin")
    # 17 | click | id=save-button |
    self.driver.find_element(By.ID, "save-button").click()
    self.driver.implicitly_wait(3)
    self.driver.find_element(By.CSS_SELECTOR, "#subtab-AdminCatalog > .link").click()
    # 9 | click | linkText=Categories |
    self.driver.find_element(By.LINK_TEXT, "Categories").click()
    # 10 | click | id=page-header-desc-configuration-add |
    table = self.driver.find_element(By.ID, "category_grid_table")
    celule = table.find_element(By.ID, "tr_2_26_6")
    self.driver.implicitly_wait(2)
    clasa = celule.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div[5]/div/div[1]/div[2]/div/div/div[2]/div/form/table/tbody/tr[7]/td[3]")
    nume = clasa.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div[5]/div/div[1]/div[2]/div/div/div[2]/div/form/table/tbody/tr[7]/td[3]/a")
    text = nume.get_attribute("innerText")
    assert "test add admin" in text

  
