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
	if (devicetype == "mobile"):
		
		options.add_experimental_option("mobileEmulation", mobile_emulation)
	
	driver = webdriver.Chrome(executable_path="/Users/TriDo/General_Code/chromedriver", chrome_options=options)
	return driver


def google_login(driver):
	driver.get("https://voice.google.com/u/0/messages")
	try:
		icon =driver.find_element_by_xpath("//a[@class='signUpLink']")
	except:
		return
	
	icon.click()
	form = driver.find_element_by_xpath("//input[@id='Email']")
	form.clear()
	form.send_keys("secret.kingston@gmail.com")
	
	driver.find_element_by_xpath("//input[@id='next']").click()
	while True:
		try:
			form = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "Passwd")))
			form.clear()
			form.send_keys("conchobang2")
			driver.find_element_by_xpath("//input[@id='signIn']").click()
			time.sleep(0.1)
			# pickle.dump(driver.get_cookies(), open("cookies.pkl", "wb"))
			break;
		except:
			print("Waiting....")
def send_sms(driver,phoneNumber,message):
	# print(driver.page_source)
	# ini= WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,"md-body-1")))
	# ini.click()
	count=0;
	while True:
		try:
			driver.find_element_by_xpath("//div[@class='md-body-1']").click()
			time.sleep(0.1)
			for i in range(0,len(phoneNumber),1):
				#input number
				number = driver.find_element_by_xpath("//input[@id='input-0']")
				number.clear()
				number.send_keys(str(phoneNumber[i]))
				time.sleep(0.5)
				number.send_keys(Keys.RETURN)
				time.sleep(0.2)
				
				#send message
				messageArea = driver.find_element_by_tag_name("textarea")
				messageArea.clear()
				messageArea.send_keys(message[i])
				driver.find_elements_by_css_selector('div.uYPEqb-H9tDt')[2].click()
				time.sleep(0.2)

			break
		except:
			count+=1;
			if(count >=100):
				print("time out...!Plz contact admin")
				break
			print("Waiting....")
	
def sms(number,message):
	"MAIN sms function to call"
	url='https://voice.google.com/u/0/messages'
	driver =getDriver("desktop")
	google_login(driver)
	driver.get("https://voice.google.com/u/0/messages")
	send_sms(driver,number,message)
	
	time.sleep(5)
	driver.close()
	
sms([3475831270],["iu cưng hehehkakakka"])