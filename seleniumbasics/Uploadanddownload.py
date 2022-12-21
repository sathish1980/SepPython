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

class uploadanddownload():

    def uploadanddownloadimplementation(self):
        self.driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("https://cleartax.in/paytax/UploadForm16")
        self.driver.find_element(by=By.XPATH,value=
            "(//div[@class='input-file-upload-hover-placeholder']//parent::div)[1]").click()
        pyperclip.copy("D:\\Besant\\JAVA\\selenium Tutorial.pdf")
        time.sleep(2)
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.press('enter')
        print("uploaded sucessfully")

    def downdefaultlocation(self):
        self.driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("https://www.leafground.com/grid.xhtml")
        self.driver.find_element(by=By.ID,value="form:j_idt93").click()
        time.sleep(5)

    def downloadinspecificdirectoty(self):
        options = webdriver.ChromeOptions()
        browser = {
            "download.default_directory": "C:\\Users\\sathishkumar\\PycharmProjects\\SepPythonBasiconline\\Downloadfile\\"}
        options.add_experimental_option("prefs", browser)
        options.add_argument("--start-maximized")
        #driver = webdriver.Chrome('D:\Software\chromedriver_win32\chromedriver.exe', options=options)
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        #self.driver.maximize_window()
        self.driver.get("https://www.leafground.com/grid.xhtml")
        self.driver.find_element(by=By.ID, value="form:j_idt93").click()
        time.sleep(5)


obj=uploadanddownload()
obj.downloadinspecificdirectoty()