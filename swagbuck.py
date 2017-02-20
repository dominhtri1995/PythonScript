from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import pickle
from bs4 import BeautifulSoup
import random

def getDriver(devicetype):
	options = webdriver.ChromeOptions()
	mobile_emulation = {"deviceName": "Google Nexus 5"}
	options.add_argument("user-data-dir=/Users/TriDo/Library/Application Support/Google/Chrome/Default")
	if (devicetype == "mobile"):
		options.add_experimental_option("mobileEmulation", mobile_emulation)
	
	driver = webdriver.Chrome(executable_path="/Users/TriDo/General_Code/chromedriver", chrome_options=options)
	return driver

def search(driver):
	listWord=["tri","anh","marron5","adam","levine","behati","candice","swag","nguyenthu","baby","victoria",
			  "cai gi","bing","microsft","stock","forex","finance","color","hottest news","okay"]
	for i in range (0,100,1):
		form = driver.find_element_by_xpath("//input[@id='sbGlobalNavSearchInputWeb']")
		form.clear()
		keyword=random.randrange(0,len(listWord),1)
		form.send_keys(listWord[keyword]+str(i))
		form.send_keys(Keys.RETURN)
		time.sleep(1)
		
driver= getDriver("desktop")
driver.get("http://www.swagbucks.com/?sfp=h&t=w&p=1&isHomeMain=true&q=abc")
search(driver)
		