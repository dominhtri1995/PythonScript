from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import  pandas as pd
import requests

url="https://www.vndirect.com.vn/portal/bang-can-doi-ke-toan/pvs.shtml"
driver = webdriver.Chrome(executable_path="/Users/TriDo/General_Code/chromedriver")
# driver =webdriver.Firefox()
#/Users/TriDo/Library/Application Support/Google/Chrome/Default
driver.get(url)


year_mode = driver.find_element_by_name("searchObject.fiscalQuarter")
all_options= year_mode.find_elements_by_tag_name("option")
for option in all_options:
	if(option.get_attribute("value")=="IN_YEAR"):
		option.click()

xem = driver.find_element_by_xpath("//input[@class='iButton autoHeight']")
xem.click()

html=driver.page_source
df = pd.read_html(html)
# soup =BeautifulSoup(html)
# print(soup.prettify())
df=df[1]
print(df)
df =df.set_index(0)
df.to_csv("output.csv",sep="\t")