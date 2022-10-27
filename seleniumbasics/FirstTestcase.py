import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


class firstTestcase():

    def firstclass(self,web=None):
       # self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=web)
       # time.sleep(1)
        self.driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()), options=web)
        self.driver.quit()

obj=firstTestcase()
obj.firstclass()