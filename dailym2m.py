import os
from selenium import webdriver
import requests
from os.path import abspath
from os import path
from time import sleep
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait
import csv
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


#DRIVER = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe'
DRIVER = 'chromedriver'
chrome_options = webdriver.ChromeOptions()

chrome_options.add_argument("--start-maximized")

#path di bawah ini C:/Users/BN001166774/AppData/Local/Google/Chrome/User Data/Default/ dapat di cek "chrome://version/"     
chrome_options.add_argument("user-data-dir=C:/Users/Rifan/AppData/Local/Google/Chrome/User Data/Default/") # Path to your chrome profile or you can open chrome and type: "chrome://version/" on URL

driver = webdriver.Chrome(DRIVER, chrome_options=chrome_options)

driver.get('http://newbips.ibpa.co.id/MtMPriceYield/DailyMtM/CorporateBond/Series.aspx')

for x in range(100):
    time.sleep(0.25)

driver.get('http://newbips.ibpa.co.id/MtMPriceYield/DailyMtM/CorporateBond/Series.aspx')

for x in range(8):
    time.sleep(0.25)




for q in range (4000):
    for x in range(20):
        time.sleep(0.25)
    input_tanggal = driver.find_element_by_id('dnn_ctr540_Series_CB_radDate_dateInput')
    input_tanggal.clear()
    bukafilenyadulu = open('tanggal.txt','r')
    terusbacalinenya = bukafilenyadulu.read().split()
    input_tanggal.send_keys(terusbacalinenya[q])
    input_tanggal.send_keys(Keys.RETURN)
    for x in range(4):
        time.sleep(0.25)
    try:
        driver.find_element_by_css_selector("A[id='dnn_ctr540_Series_CB_btnExport']").click()
        for x in range(20):
            time.sleep(0.25)
    except:
        pass