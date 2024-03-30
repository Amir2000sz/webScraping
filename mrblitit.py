from types import TracebackType
from typing import Type
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import os 

class mrbilit(webdriver.Chrome):
    def __init__(self,checker):
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
        


