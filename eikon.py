from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import  pandas as pd
import requests
import pickle
import time

options = webdriver.ChromeOptions()
options.add_argument("user-data-dir=/Users/TriDo/Library/Application Support/Google/Chrome/Default") #Path to your chrome profile
url="https://apac1.login.cp.thomsonreuters.net/auth/cdcservlet?theme=charcoal&goto=https%3A%2F%2Fapac1.apps.cp.thomsonreuters.com%3A443%2Fweb%2FApps%2FCorp%3Fs%3DUN%26st%3DRIC%26app%3Dtrue&RequestID=112027117&MajorVersion=1&MinorVersion=0&ProviderID=https%3A%2F%2Fapac1.proxy.cp.thomsonreuters.com%3A443%2Famagent&IssueInstant=2017-02-10T07%3A39%3A25Z"
driver = webdriver.Chrome(executable_path="/Users/TriDo/General_Code/chromedriver",chrome_options=options)
# driver =webdriver.Firefox()
driver.get(url)

username = driver.find_element_by_xpath("//input[@id='AAA-AS-SI1-SE003']")
username.send_keys("eikon9.rmit@rmit.edu.vn")

pwd = driver.find_element_by_xpath("//input[@id='AAA-AS-SI1-SE006']")
pwd.send_keys("Zur2&5!?")


submit = driver.find_element_by_xpath("//div[@class='button_img button_75 button_75_enabled']")
submit.click()
time.sleep(2)

driver.switch_to.frame("AppFrame")
driver.switch_to.frame(3)
driver.switch_to.frame(0)

html = driver.page_source
print(html)