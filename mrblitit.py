from types import TracebackType
from typing import Type
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os 
import time
class mrbilit(webdriver.Chrome):
    def __init__(self,checker,origin=None,destinition=None,date=None):
        self.date = date
        self.origin = origin
        self.destination = destinition
        self.chek = checker
        os.environ['PATH'] += r"f:\chrome-win64\chrome-win64"
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)
        super(mrbilit , self).__init__(options=chrome_options)
        with open("mrbilit.txt",'r') as file :
            self.address = file.readlines()
            
    def run(self,i):
       self.get(f"{self.address[i]}")

    def __exit__(self, exc_type , exc_val , exc_tb):
        if self.chek == True :
            self.quit()
    def choose_type(self,type="bus"):
       
        if type.lower() == "bus":
            self.run(2)
            typeB = self.find_element(by=By.XPATH, value="/html/body/div/div/div[2]/div[2]/div[2]/div[1]/div[1]/div/ul/li[4]")
            typeB.click()
            # self.bus("out")
        if type.lower() == "plane":
            self.run(1)
            typeP = self.find_element(by = By.XPATH , value="/html/body/div/div/div[2]/div[2]/div[2]/div[1]/div[1]/div/ul/li[1]")
            typeP.click()
        if type.lower() == "car":
            self.run(3)
            typeC = self.find_element(by = By.XPATH , value="/html/body/div/div/div[2]/div[2]/div[2]/div[1]/div[1]/div/ul/li[5]")
            typeC.click()
        if type.lower() == "train":
            self.run(4)
            typeT = self.find_element(by = By.XPATH , value="/html/body/div/div/div[2]/div[2]/div[2]/div[1]/div[1]/div/ul/li[3]")
            typeT.click()

    def choose_origin(self):

        origin = self.find_element(by=By.XPATH , value="/html/body/div/div/div[2]/div[2]/div[2]/form/div[2]/div[1]/div[1]/div/div/div[1]/div/label/input")
        self.implicitly_wait(10)
        origin.click()
        origin.send_keys(self.origin)
        wait = WebDriverWait(self, 10)
        suggestion_list = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/div[2]/div[2]/div[2]/form/div[2]/div[1]/div[1]/div/div/div[2]/div/div/div[2]")))
        time.sleep(1)
        firstOption = self.find_element(by=By.XPATH, value="/html/body/div/div/div[2]/div[2]/div[2]/form/div[2]/div[1]/div[1]/div/div/div[2]/div/div/div[2]")
        firstOption.click()

    def choose_destination(self):
        desti = self.find_element(By.XPATH,"/html/body/div/div/div[2]/div[2]/div[2]/form/div[2]/div[1]/div[2]/div/div/div[1]/div/label/input")
        self.implicitly_wait(10)
        desti.click()
        desti.send_keys(self.destination)
        waitD = WebDriverWait(self, 10)
        suggestion_list2 = waitD.until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/div[2]/div[2]/div[2]/form/div[2]/div[1]/div[2]/div/div/div[2]/div/div/div[2]")))
        time.sleep(1)
        firstOptionD = self.find_element(by=By.XPATH, value="/html/body/div/div/div[2]/div[2]/div[2]/form/div[2]/div[1]/div[2]/div/div/div[2]/div/div/div[2]")
        firstOptionD.click()
    
    def choose_date(self):
        waitDate = WebDriverWait(self, 10)
        suggestion_list_Date = waitDate.until(EC.visibility_of_element_located((By.CLASS_NAME, "mr-datepicker-container")))
        while True:
            buttonOfDAte = self.find_element(By.XPATH , "/html/body/div/div/div[2]/div[2]/div[2]/form/div[2]/div[2]/div/div[1]/div[1]/div")
            buttonOfDAte.click()
            self.implicitly_wait(5)
            try:
                
                date = self.find_elements(By.CLASS_NAME , "day-container")
                date[self.date-1].click()
                break
            except :
                print("the date you have choosen is not available")
                break
    
    def search(self):
        searchbut = self.find_element(By.XPATH , '//*[@id="search-bus"]/div[2]/div[4]/button' )
        searchbut.click()
    def checkAvailable(self):
        try:
            self.implicitly_wait(15)
            parent_div = self.find_element(By.CLASS_NAME, "card-section-container")
            child_div = parent_div.find_elements(By.CLASS_NAME , "trip-card-container")
            print(f"there are {len(child_div)-1} options available right now")
        except :
            print(f"there is no bus in this date")
            