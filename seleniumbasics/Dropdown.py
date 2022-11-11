import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
class dropdown():

    def singleselect(self):
        self.driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("https://chercher.tech/practice/practice-dropdowns-selenium-webdriver")
        product=Select(self.driver.find_element(by=By.XPATH,value="(//*[@class='col-lg-3'])[1]"))
        product.select_by_index(2)
        time.sleep(2)
        product.select_by_value("Microsoft")
        time.sleep(2)
        product.select_by_visible_text("Yahoo")

    def multiselect(self):
        product = Select(self.driver.find_element(by=By.XPATH, value="(//*[@class='col-lg-3'])[3]"))
        if product.is_multiple == True:
            product.select_by_index(2)
            product.select_by_value("donut")
            product.select_by_visible_text("Pizza")
            time.sleep(2)
            product.deselect_by_index(1)
            time.sleep(2)
            product.deselect_all()

obj = dropdown()
obj.singleselect()
obj.multiselect()