from selenium import webdriver
import pandas as pd
import tkinter
from tkinter import *
import threading
from threading import Semaphore

def get_statement(type, ticker, excel):
	lock.acquire()
	for i in range(0,2):
		try:
			driver = webdriver.Chrome(executable_path="/Users/TriDo/General_Code/chromedriver")
			driver.set_window_position(5000, 0)
			if (type == "bs"):
				url = "https://www.vndirect.com.vn/portal/bang-can-doi-ke-toan/" + ticker + ".shtml"
			elif (type == "ic"):
				url = "https://www.vndirect.com.vn/portal/bao-cao-ket-qua-kinh-doanh/" + ticker + ".shtml"
			elif (type == "cf"):
				url = "https://www.vndirect.com.vn/portal/bao-cao-luu-chuyen-tien-te/" + ticker + ".shtml"
			driver.get(url)
			
			year_mode = driver.find_element_by_name("searchObject.fiscalQuarter")
			all_options = year_mode.find_elements_by_tag_name("option")
			for option in all_options:
				if (option.get_attribute("value") == "IN_YEAR"):
					option.click()
			
			xem = driver.find_element_by_xpath("//input[@class='iButton autoHeight']")
			xem.click()
			
			html = driver.page_source
			df = pd.read_html(html)
			df = df[1]
			# print(df)
			df = df.set_index(0)
			df.to_excel(excel, type)
			excel.save()
		except:
			driver.close()
			continue
		driver.close()
		break
		
	lock.release()


def get_data(ticker, bs, ic, cf):
	ticker = ticker.upper()
	tickers = ticker.split(",")
	for ticker in tickers:
		
		excelwriter = pd.ExcelWriter(ticker + ".xlsx")
		print(ticker)
		if (bs == 1):
			# text.insert(INSERT,"Getting Balance Sheet")
			thread1 = myThread(1, "bs",ticker,excelwriter)
			thread1.start()
			threads.append(thread1)
		if (ic == 1):
			thread2 = myThread(1, "ic", ticker, excelwriter)
			thread2.start()
			threads.append(thread2)
		if (cf == 1):
			thread3 = myThread(1, "cf", ticker, excelwriter)
			thread3.start()
			threads.append(thread3)

class myThread(threading.Thread):
	def __init__(self, threadID, name, ticker,excelwriter):
		threading.Thread.__init__(self)
		self.threadID = threadID
		self.name = name
		self.ticker = ticker
		self.excelwriter= excelwriter
	def run(self):
		print("Starting " + self.name)
		get_statement(self.name, self.ticker, self.excelwriter)

###********** MAIN PROGRAM *************##
#global variable go here
lock = Semaphore(3)
threads = []

######### GUI go here #########
top = tkinter.Tk()
top.wm_title("Whirlpool-Data")
screen_width = top.winfo_screenwidth()
screen_height = top.winfo_screenheight()

    # calculate position x and y coordinates
x = (screen_width/2) - (400/2)
y = (screen_height/2) - (400/2)
top.geometry('%dx%d+%d+%d' % (400, 400, x, y))

# Code to add widgets will go here...
L1 = Label(top, text="Ticker")
L1.pack(side=LEFT)
E1 = Entry(top, bd=5)
E1.pack(side=LEFT)

# Option which type of financial statement
CheckVar1 = IntVar()
CheckVar2 = IntVar()
CheckVar3 = IntVar()
C1 = Checkbutton(top, text="Balance sheet", variable=CheckVar1, \
				 onvalue=1, offvalue=0, height=2, \
				 width=20)
C2 = Checkbutton(top, text="Income Statement", variable=CheckVar2, \
				 onvalue=1, offvalue=0, height=2, \
				 width=20)
C3 = Checkbutton(top, text="CashFlow", variable=CheckVar3, \
				 onvalue=1, offvalue=0, height=2, \
				 width=20)
C1.pack();
C1.select()
C2.pack();
C2.select()
C3.pack();
C3.select()
# Button
B = tkinter.Button(top, text="Download", height =9,
				   command=lambda: get_data(E1.get(), CheckVar1.get(), CheckVar2.get(), CheckVar3.get()))
B.pack()



top.mainloop()
