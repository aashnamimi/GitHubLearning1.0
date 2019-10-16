from selenium.webdriver.common.by import By
from selenium import  webdriver
class Locators():
  
    def __init__(self, driver):
        self.driver = driver
        self.username_textbox = (By.ID, "txtUsername")
        self.password_textbox=(By.ID,"txtPassword")
        self.login_button=(By.ID,"btnLogin")
        self.username_textbox_id = "txtUsername"
        self.password_textbox_id = "txtPassword"
        self.login_button_id = "btnLogin"

    def enter_username(self,username):
        
        #self.driver.find_element_by_id(self.username_textbox).send_keys(username)
        self.username_textbox.send_keys(username)
        #self.driver.find_element_by_id(self.username_textbox_id).send_keys(username)

    def enter_password(self,password):
        self.driver.find_element_by_id(self.password_textbox_id).send_keys(password)

    def click_login(self):
        self.driver.find_element_by_id(self.login_button_id).click()







