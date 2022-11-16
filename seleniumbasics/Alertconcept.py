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

class alertconepct():

    def alertimplementation(self):
        self.driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("https://www.leafground.com/")
        #self.driver.find_element(by=By.XPATH,value="//*[@id='menuform:j_idt39']").click()
        #self.driver.find_element(by=By.XPATH,value="//*[@id='menuform:j_idt39']//li[@id='menuform:m_overlay']").click()
        mouseactions = ActionChains(self.driver)
        mouseactions.move_to_element(self.driver.find_element(by=By.XPATH,value="//*[@id='menuform:j_idt39']")).click().move_to_element(self.driver.find_element(by=By.XPATH,value="//*[@id='menuform:j_idt39']//li[@id='menuform:m_overlay']")).click().perform()
        WebDriverWait(self.driver, 60).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='j_idt88:j_idt91']")))
        self.driver.find_element(by=By.XPATH,value="//*[@id='j_idt88:j_idt91']").click()
        time.sleep(1)
        alerts=self.driver.switch_to.alert
        alerts.accept() # click ok ,yes .iagree ..
        self.driver.find_element(by=By.ID,value="j_idt88:j_idt93").click()
        time.sleep(1)
        alerts = self.driver.switch_to.alert
        alerts.dismiss() # click cancel , No , i disagree
        self.driver.find_element(by=By.ID,value="j_idt88:j_idt104").click()
        time.sleep(1)
        alerts = self.driver.switch_to.alert
        alerts.send_keys("Besant technology")
        alerts.accept()

        # sweet alert
        self.driver.find_element(by=By.ID,value="j_idt88:j_idt95").click()
        time.sleep(1)
        self.driver.find_element(by=By.ID,value="j_idt88:j_idt98").click()

        self.driver.find_element(by=By.ID,value="j_idt88:j_idt100").click()
        time.sleep(1)
        self.driver.find_element(by=By.XPATH,value="//*[@id='j_idt88:j_idt101']//*[@aria-label='Close']//span").click()



obj=alertconepct()
obj.alertimplementation()