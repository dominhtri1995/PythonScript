from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import pickle
from bs4 import  BeautifulSoup

def getDriver(devicetype):
	options = webdriver.ChromeOptions()
	mobile_emulation = {"deviceName": "Google Nexus 5"}
	options.add_argument("user-data-dir=/Users/TriDo/Library/Application Support/Google/Chrome/Default")
	if(devicetype =="mobile"):
		options.add_experimental_option("mobileEmulation", mobile_emulation)
		
	driver = webdriver.Chrome(executable_path="/Users/TriDo/General_Code/chromedriver", chrome_options=options)
	return driver
def bing_login(driver):
	driver.get(
		"https://login.live.com/login.srf?wa=wsignin1.0&rpsnv=13&ct=1486454561&rver=6.7.6631.0&wp=MBI&wreply=https%3a%2f%2fwww.bing.com%2fsecure%2fPassport.aspx%3frequrl%3dhttp%253a%252f%252fwww.bing.com%252f%253fwlexpsignin%253d1&lc=1033&id=264960")
	form = driver.find_element_by_name("loginfmt")
	form.send_keys("nikki.hoang91@gmail.com")
	
	driver.find_element_by_xpath("//input[@id='idSIButton9']").click()
	
	while True:
		try:
			form = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.NAME, "passwd")))
			form.clear()
			form.send_keys("knguyen91")
			driver.find_element_by_xpath("//input[@id='idSIButton9']").click()
			time.sleep(0.1)
			pickle.dump(driver.get_cookies(), open("cookies.pkl", "wb"))
			break;
		except:
			print("Waiting....")

def get_bing_rewards(html):
	soup = BeautifulSoup(html,"lxml")
	dt=soup.find_all('span',{'class':'details'})
	for i in range(0,3,1):
		string =[]
		for st in dt[i].strings:
			string.append(st)
		print(string[2]+": "+string[0]+string[1])
	
driver = getDriver("desktop")
bing_login(driver)

for i in range(1,35,1):
	form=driver.find_element_by_xpath("//input[@class='b_searchbox']")
	form.clear()
	form.send_keys("cai long gi day",i*i)
	driver.find_element_by_class_name("b_searchboxSubmit").click()
	time.sleep(0.1)

time.sleep(1)
driver.close()

#############Mobile
driver= getDriver("mobile")
bing_login(driver)


for i in range(1,30,1):
	form=driver.find_element_by_xpath("//input[@id='sb_form_q']")
	form.clear()
	form.send_keys("cai long gi day",i*77)
	# driver.find_element_by_xpath("//input[@id='sbBtn']").click()
	form.send_keys(Keys.RETURN)
	time.sleep(0.1)
time.sleep(1)
driver.close()
##########
driver=getDriver("desktop")
bing_login(driver)
driver.find_element_by_xpath("//span[@class='id_avatar sw_meIc']").click()
frame_reward= driver.find_element_by_xpath("//iframe[@id='bepfm']")
driver.switch_to.frame(frame_reward)
html =driver.page_source
get_bing_rewards(html)