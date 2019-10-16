import pytest
from selenium import webdriver
import time
import Resources.Locators
from selenium.webdriver.common.by import By
import Resources.TestData


@pytest.fixture()
def test_setup():
    global driver
   # chrome_options = webdriver.ChromeOptions()    
    driver = webdriver.Chrome(executable_path=Resources.TestData.TestData.CHROME_EXECUTABLE_PATH)
    # driver = webdriver.Chrome(ChromeDriverManager.install())
    #driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver.exe")
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield
    driver.close()
    driver.quit()
    print("test complete")


def test_login_valid(test_setup):

    driver.get("https://opensource-demo.orangehrmlive.com/")
    time.sleep(5)
    login = Resources.Locators.Locators(driver)
    login.enter_username("Admin")
    login.enter_password("admin")
  
