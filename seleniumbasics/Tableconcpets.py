import time

import pyautogui
import pyperclip

import time

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
class tableconcept():

    def tableimplementation(self,actualstatus):
        self.driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("https://leafground.com/table.xhtml")
        Totalpages=self.driver.find_elements(by=By.XPATH,value="//*[@class='ui-paginator-pages']//a")
        for eachpage in range(1,len(Totalpages)+1):
            eachpagewebelement=self.driver.find_element(by=By.XPATH,value="//*[@class='ui-paginator-pages']//a["+str(eachpage)+"]")
            #time.sleep(2)
            self.driver.execute_script("arguments[0].scrollIntoView();", eachpagewebelement)
            #self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            #WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, "//*[@class='ui-paginator-pages']//a")))
            eachpagewebelement.click()
            time.sleep(1)
            basepath="//*[@id='form:j_idt89']//tbody//tr"
            Totalrows=self.driver.find_elements(by=By.XPATH,value=basepath)
            for eachrow in range(1,len(Totalrows)+1):
                #self.driver.find_elements(by=By.XPATH, value=basepath+"["+str(eachrow)+"]")
                status=self.driver.find_element(by=By.XPATH,value=basepath+"["+str(eachrow)+"]//td[5]//span[contains(@class,'customer-badge')]").text
                if(status==actualstatus):
                    country=self.driver.find_element(by=By.XPATH,value=basepath+"["+str(eachrow)+"]//td[2]//span[3]").text
                    name =self.driver.find_element(by=By.XPATH,value=basepath+"["+str(eachrow)+"]//td[1]").text
                    print(country , name)

obj=tableconcept()
obj.tableimplementation("QUALIFIED")

