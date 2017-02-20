import re
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import time

def getDriver(devicetype):
	options = webdriver.ChromeOptions()
	mobile_emulation = {"deviceName": "Google Nexus 5"}
	options.add_argument("user-data-dir=/Users/TriDo/Library/Application Support/Google/Chrome/Default")
	if (devicetype == "mobile"):
		options.add_experimental_option("mobileEmulation", mobile_emulation)
	
	driver = webdriver.Chrome(executable_path="/Users/TriDo/General_Code/chromedriver", chrome_options=options)
	return driver


def crawl(driver):
	driver.find_element_by_xpath("//button[@id='paginationNext']").click()

def clean_string(string):
	string = string.strip()
	string = " ".join(string.split())
	return string


def get_data(html):
	"get room"
	soup=BeautifulSoup(html,"lxml")
	li= soup.find_all('li',{"class":"ssr-search-result"})
	for l in li:
		link=l.find('a')
		if(link==None):
			continue
		ul=link.find('ul',{'class':'property-info-container'})
		name=ul.find('h3')
		hotel_url.append("www.agoda.com"+link['href'])
		hotel_name.append(clean_string(name.text))
		
	count =0;
	for link in hotel_url:
		print("hotel no :",count+1)
		driver.get("http://"+link)
		subSoup=BeautifulSoup(driver.page_source,"lxml")
		div= subSoup.find_all('div',{'class':'sub-section no-margin padding-bottom'})
		
		if(not div):
			print("ko co div "+link)
			count += 1
			room.append("NaN")
			continue
		found=0;
		for subdiv in div:
			for d in subdiv.find_all('div'):
				if("Number of rooms :" in d.text):
					num=d.find('strong').text
					room.append(clean_string(num))
					found=1
					continue
		if(found==0):
			room.append("NaN")
		count += 1
		
	print(hotel_url)
	print(room)
	print(hotel_name)
	#crawl(driver)
	
########***** Main Program #######*******
start_time=time.time()
url="https://www.agoda.com/pages/agoda/default/DestinationSearchResult.aspx?selectedproperty=301413&checkIn=2017-03-13&los=1&cid=-1&city=17190&pagetypeid=103&origin=US&tag=&gclid=&aid=130243&userId=435f9bc5-75cf-484d-abbd-e8bf840f7060&languageId=1&sessionId=eepn4pboc1iohhqr2tneia4f&storefrontId=3&currencyCode=USD&htmlLanguage=en-us&trafficType=User&cultureInfoName=en-US&checkOut=2017-03-14&rooms=1&adults=1&children=0&ckuid=435f9bc5-75cf-484d-abbd-e8bf840f7060"
driver=getDriver("desktop")
driver.get(url)

hotel_url=[];room=[];hotel_name=[]
html = driver.page_source
get_data(html)

## Save to csv
d={'Hotel_Name':hotel_name,
   'Room':room,
   'Url': hotel_url}

df= pd.DataFrame.from_dict(d,orient='index')
df=df.transpose()
df.to_csv("agoda.csv",index=False,sep="\t")
print("Done in time: ",time.time()-start_time)
driver.close()