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
class checkbox():

    def chboximplementation(self):
        self.driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("https://www.leafground.com/checkbox.xhtml")
        displayedornot = self.driver.find_element(by=By.XPATH, value="//*[@id='j_idt87:j_idt91']//div[2]").is_displayed()
        print("isdisplayed: ",displayedornot)
        selectedornot=self.driver.find_element(by=By.XPATH,value="//*[@id='j_idt87:j_idt91']//div[2]").is_selected()
        print("isselected: ", selectedornot)
        enabledornot = self.driver.find_element(by=By.XPATH, value="//*[@id='j_idt87:j_idt91']//div[2]").is_enabled()
        print("isenabled: ", enabledornot)
        if selectedornot == False and displayedornot == True and enabledornot==True:
            self.driver.find_element(by=By.XPATH,value="//*[@id='j_idt87:j_idt91']//div[2]").click()
        else:
            print("this is already selected")
        afterselected = self.driver.find_element(by=By.XPATH, value="//*[@id='j_idt87:j_idt91']//div[2]").is_selected()
        print("isselectedpostaction: ", afterselected)

        disabledelement = self.driver.find_element(by=By.XPATH, value="//*[@id='j_idt87:j_idt102']//div[2]").is_enabled()
        print(disabledelement)

        print(self.driver.title)
        print(self.driver.current_url)
        buttontittle=self.driver.find_element(by=By.XPATH,value="(//*[contains(@class,'ui-fluid')]//h5)[5]").text
        print(buttontittle)
        javascript=self.driver.find_element(by=By.XPATH,value="//*[@for='j_idt87:basic:2']").text
        print(javascript)
        classatrribute=self.driver.find_element(by=By.XPATH,value="//*[@id='j_idt87:basic']").get_attribute("class")
        print(classatrribute)
        print(self.driver.current_window_handle)
        print(self.driver.window_handles)



obj=checkbox()
obj.chboximplementation()