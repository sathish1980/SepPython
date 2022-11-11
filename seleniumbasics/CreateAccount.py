import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.support import expected_conditions as EC


class createAccount():

    def createaccount(self):
        self.driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("https://www.facebook.com/")
        self.driver.find_element(by=By.XPATH,value="//*[@data-testid='open-registration-form-button']").click()
        self.driver.implicitly_wait(60)
        self.driver.find_element(by=By.NAME,value="firstname").send_keys("kumar")
        self.driver.find_element(by=By.NAME, value="lastname").send_keys("kumar")
        self.driver.find_element(by=By.NAME, value="reg_email__").send_keys("kumar.sathish189@gmail.com")
        time.sleep(2)
        WebDriverWait(self.driver, 60).until(
            EC.presence_of_element_located((By.NAME, "reg_email_confirmation__")))
        self.driver.find_element(by=By.NAME, value="reg_email_confirmation__").send_keys("kumar.sathish189@gmail.com")
        self.driver.find_element(by=By.XPATH,value="//*[text()='Custom']//parent::span//input").click()
        WebDriverWait(self.driver, 60).until(
            EC.presence_of_element_located((By.NAME, "preferred_pronoun")))



obj=createAccount()
obj.createaccount()