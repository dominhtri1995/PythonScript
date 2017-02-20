from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import pickle
from bs4 import  BeautifulSoup
import pandas as pd

def getDriver(devicetype):
	options = webdriver.ChromeOptions()
	mobile_emulation = {"deviceName": "Google Nexus 5"}
	options.add_argument("user-data-dir=/Users/TriDo/Library/Application Support/Google/Chrome/Default")
	if (devicetype == "mobile"):
		options.add_experimental_option("mobileEmulation", mobile_emulation)
	
	driver = webdriver.Chrome(executable_path="/Users/TriDo/General_Code/chromedriver", chrome_options=options)
	return driver

def next(driver):
	driver.find_element_by_xpath("//li[@class='nav-previous']").click()

def clean_string(string):
	string = string.strip()
	string = " ".join(string.split())
	return string
def get_data(html):
	######Beautiful Soup from here #####
	soup = BeautifulSoup(html, "lxml")
	articles = soup.find_all("article")
	for article in articles:
		link = article.find('a')
		image = link.find('img')
		link_href.append(link['href'])
		img_url.append(image['src'])
		
		count=0;
		
		link1=link.find_next('a')
		titleText =clean_string(link1['title'])
		title.append(titleText)
		div=article.find_all('div')
		div=div[len(div)-1]
		excerpt.append(clean_string(div.text))
		
########***** Main Program #######*******
url="http://www.politicalears.com/#"
driver=getDriver("desktop")
driver.get(url)
#list
title=[];img_url=[];link_href=[];excerpt=[];

for i in range (0,20,1):
	print("Getting page: ",i+1)
	html=driver.page_source
	get_data(html)
	next(driver)
	time.sleep(0.1)

driver.close()

## Save to csv
d={'title': title,
   'link': link_href,
   'excerpt': excerpt,
   'image':img_url}

print(excerpt)
print(title)
print(len(title))
print(len(img_url))
print(len(link_href))
print(len(excerpt))

pd = pd.DataFrame.from_dict(d,orient='index')
pd=pd.transpose()
pd.to_csv('politicalears.csv',index=False,sep="\t")
