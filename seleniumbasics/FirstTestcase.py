import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


class firstTestcase():

    def firstclass(self,web=None):
       # self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=web)
       # time.sleep(1)
        self.driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()), options=web)
        self.driver.maximize_window()
        #self.driver.minimize_window()
        #self.driver.set_window_size(700,300)
        self.driver.get("https://www.facebook.com/")
        #self.driver.find_element(by=By.ID,value="email").send_keys("sathishkumar")

        self.driver.find_element(by=By.NAME, value="email").send_keys("kumar.sathish189@gmail.com")

        self.driver.find_element(by=By.NAME, value="email").clear()

        self.driver.find_element(by=By.NAME, value="email").send_keys("latestvalue")

        self.driver.find_element(by=By.NAME, value="email").send_keys("today")
        self.driver.find_element(by=By.CSS_SELECTOR,value="input#email").send_keys("Bycssselector")
        self.driver.find_element(by=By.CSS_SELECTOR,value="input[data-testid='royal_email']").send_keys("thirdtype")
        self.driver.find_element(by=By.XPATH ,value="//input[@id='email']").send_keys("name")
        self.driver.find_element(by=By.XPATH,value="//*[contains(@id,'u_0_9')]").send_keys("contains")
        self.driver.find_element(by=By.XPATH,value="//*[starts-with(@id,'u_0_9') or @name='login']").send_keys("startswith and logical")
        self.driver.find_element(by=By.XPATH,value="//*[text()='Log in' and @name='login']").send_keys("text")
        #self.driver.find_element(by=By.CSS_SELECTOR, value="input.inputtext _55r1 _6luy").send_keys("Bycssselector")
        self.driver.find_element(by=By.LINK_TEXT,value="Forgotten password?").click()

        self.driver.find_element(by=By.PARTIAL_LINK_TEXT, value="ten").click()
        self.driver.find_element(by=By.XPATH,value="(//*[@id='day']//following::option[@value='2'])[1]")
        #self.driver.find_element(by=By.CLASS_NAME,value="inputtext _55r1 _6luy").send_keys("sathish")

        """self.driver.get("https://www.gmail.com/")
        self.driver.back()
        self.driver.forward()
        self.driver.refresh()
        self.driver.quit()"""

obj=firstTestcase()
obj.firstclass()