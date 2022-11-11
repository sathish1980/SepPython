import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.support import expected_conditions as EC

class listconceptdropdown():
    basepath = "//*[@id='react-autowhatever-1']//ul//li"
    def listconceptimplementation(self,expectdvalue):
        self.driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("https://www.makemytrip.com/")
        time.sleep(2)
        self.driver.find_element(by=By.XPATH,value="//*[@for='fromCity']").click()
        WebDriverWait(self.driver, 60).until(EC.presence_of_element_located((By.XPATH, self.basepath+"[1]")))
        listofcites=self.driver.find_elements(by=By.XPATH,value=self.basepath)
        print(len(listofcites))
        for eachvalue in range(1,len(listofcites)+1):
            actualstring=self.driver.find_element(by=By.XPATH,value=self.basepath+"["+str(eachvalue)+"]//div[2]").text
            print(actualstring)
            if actualstring == expectdvalue:
                self.driver.find_element(by=By.XPATH,value=self.basepath+"["+str(eachvalue)+"]").click()
                break
    def tolocation(self,tolocationcalue):

        WebDriverWait(self.driver, 60).until(EC.presence_of_element_located((By.XPATH, self.basepath + "[1]")))
        listofcites = self.driver.find_elements(by=By.XPATH, value=self.basepath)
        print(len(listofcites))
        for eachvalue in range(1, len(listofcites) + 1):
            actualstring = self.driver.find_element(by=By.XPATH,
                                                    value=self.basepath + "[" + str(eachvalue) + "]//div[2]").text
            print(actualstring)
            if actualstring == tolocationcalue:
                self.driver.find_element(by=By.XPATH, value=self.basepath + "[" + str(eachvalue) + "]").click()
                break

obj=listconceptdropdown()
obj.listconceptimplementation("PNQ")
obj.tolocation("MAA")