from types import TracebackType
from typing import Type
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os 

class mrbilit(webdriver.Chrome):
    def __init__(self,checker,origin=None,destinition=None):
        self.origin = origin
        self.destinition = destinition
        self.chek = checker
        os.environ['PATH'] += r"f:\chrome-win64\chrome-win64"
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)
        super(mrbilit , self).__init__(options=chrome_options)
        with open("mrbilit.txt",'r') as file :
            self.address = file.readlines()[0]
            
    def run(self):
       self.get(f"{self.address}")

    def __exit__(self, exc_type , exc_val , exc_tb):
        if self.chek == True :
            self.quit()
    def choose_type(self,type="bus"):
       
        if type.lower() == "bus":
            typeB = self.find_element(by=By.XPATH, value="/html/body/div/div/div[2]/div[2]/div[2]/div[1]/div[1]/div/ul/li[4]")
            typeB.click()
            self.bus("out")
        if type.lower() == "plane":
            typeP = self.find_element(by = By.XPATH , value="/html/body/div/div/div[2]/div[2]/div[2]/div[1]/div[1]/div/ul/li[1]")
            typeP.click()
        if type.lower() == "car":
            typeC = self.find_element(by = By.XPATH , value="/html/body/div/div/div[2]/div[2]/div[2]/div[1]/div[1]/div/ul/li[5]")
            typeC.click()
        if type.lower() == "train":
            typeT = self.find_element(by = By.XPATH , value="/html/body/div/div/div[2]/div[2]/div[2]/div[1]/div[1]/div/ul/li[3]")
            typeT.click()

    def bus(self,inOrOut = "in"):
        if inOrOut.lower() == "out":
            outOption = self.find_element(by=By.XPATH , value = "/html/body/div/div/div[2]/div[2]/div[2]/form/div[1]/div[1]/label[2]/div")
            outOption.click()

    def choose_origin(self):

        origin = self.find_element(by=By.XPATH , value="/html/body/div/div/div[2]/div[2]/div[2]/form/div[2]/div[1]/div[1]/div/div/div[1]/div/label/input")
        origin.send_keys(self.origin)
        wait = WebDriverWait(self, 10)
        suggestion_list = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/div[2]/div[2]/div[2]/form/div[2]/div[1]/div[1]/div/div/div[2]/div/div/div[2]")))
        
        firstOption = self.find_element(by=By.XPATH, value="/html/body/div/div/div[2]/div[2]/div[2]/form/div[2]/div[1]/div[1]/div/div/div[2]/div/div/div[2]")
        firstOption.click()