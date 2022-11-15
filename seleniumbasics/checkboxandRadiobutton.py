import pyautogui
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.actions.interaction import KEY
from selenium.webdriver.common import keys
class checkboxandradio():

    def implementation(self):
        self.driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("https://www.leafground.com/radio.xhtml")
        self.driver.find_element(by=By.XPATH,value="(//*[text()='Safari']//parent::td//div[contains(@class,'ui-radiobutton-box')])[1]").click()
    def chboximplementation(self):
        self.driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("https://www.leafground.com/checkbox.xhtml")
        self.driver.find_element(by=By.XPATH,value="//*[text()='Basic']//parent::div[contains(@class,'ui-chkbox')]").click()

obj=checkboxandradio()
obj.chboximplementation()