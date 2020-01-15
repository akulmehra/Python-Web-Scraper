from bs4 import BeautifulSoup
import urllib.request
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import csv
import time 

driver = webdriver.Chrome(executable_path = "/Users/akulmehra/Desktop/leverage/chromedriver")

driver.maximize_window()

#for i in range(1,131):

#driver.get('https://www.clearadmit.com/decisionwire/page/' + str(i) + '/')
driver.get('https://www.clearadmit.com/decisionwire/page/1/')
driver.execute_script("window.scrollTo(0,600);")
driver.implicitly_wait(30)

page = driver.page_source
soup = BeautifulSoup(page, 'html.parser')


# with open('clearadmit.csv', 'w') as writeFile: 
for i in range(2,36):
	print('############################')
	for j in range(1,9):
		# a = []
		

		try:
			x_path = '//*[@id="entries"]/div/div[2]/div/div/div/div/div[1]/div[4]/div[' + str(i) + ']/div/div[2]/div[' + str(j) + ']'
			entries = driver.find_element_by_xpath(x_path)
		# writer = csv.writer(writeFile)
		# a.append(entries.text)
		# writer.writerow(a)
			# cprint(x_path)
			print(entries.text)
		except Exception as e:
			pass

		try:
			for k in range(1,3):
				x_path_2 = '//*[@id="entries"]/div/div[2]/div/div/div/div/div[1]/div[4]/div[' + str(i) + ']/div/div[2]'
				entries_2 = driver.find_element_by_xpath(x_path_2)
				# scores = entries_2.find_element_by_tag_name('strong')
				
				print(entries_2.text)
		except Exception as f:
			pass


#if 'GPA' in data:




		
# //*[@id="entries"]/div/div[2]/div/div/div/div/div[1]/div[4]/div[2]/div/div[2]/text()[1]
# //*[@id="entries"]/div/div[2]/div/div/div/div/div[1]/div[4]/div[2]/div/div[2]/
#//*[@id="entries"]/div/div[2]/div/div/div/div/div[1]/div[4]/div[2]/div/div[2]		
#//*[@id="entries"]/div/div[2]/div/div/div/div/div[1]/div[4]/div[5]/div/div[2]/div[2]
#//*[@id="entries"]/div/div[2]/div/div/div/div/div[1]/div[4]/div[2]/div/div[2]/text()[1]
#//*[@id="entries"]/div/div[2]/div/div/div/div/div[1]/div[4]/div[3]/div/div[2]/text()
#//*[@id="entries"]/div/div[2]/div/div/div/div/div[1]/div[4]/div[4]/div/div[2]/text()

#//*[@id="entries"]/div/div[2]/div/div/div/div/div[1]/div[4]/div[2]/div/div[2]/div[7]
#

#//*[@id="entries"]/div/div[2]/div/div/div/div/div[1]/div[4]/div[2]/div/div[2]/div[2]
#//*[@id="entries"]/div/div[2]/div/div/div/div/div[1]/div[4]/div[2]/div/div[2]/div[1]
#//*[@id="entries"]/div/div[2]/div/div/div/div/div[1]/div[4]/div[3]/div/div[2]/div[1]
#//*[@id="entries"]/div/div[2]/div/div/div/div/div[1]/div[4]/div[4]/div/div[2]/div[1] 

#//*[@id="entries"]/div/div[2]/div/div/div/div/div[1]/div[4]/div[6]/div/div[2]/div[8]