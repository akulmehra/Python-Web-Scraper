from bs4 import BeautifulSoup
import urllib.request
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.action_chains import ActionChains
import csv

driver = webdriver.Chrome(executable_path = "/Users/akulmehra/Desktop/leverage/chromedriver")
driver.implicitly_wait(30)
driver.maximize_window()

csv_headings = {'University Name', 'Link'}

course_names = []
durations = []
tuition_fees = []
descriptions = []

with open('uni_links.csv', 'r') as readFile:
	reader = csv.reader(readFile)
	for row in reader:
		link = row[2]
		uni_name = row[0]
		if link not in csv_headings:
			driver.get(link)
			
			#gets rid of pop up
			try:
				driver.find_element_by_xpath('//*[@id="webpush-custom-prompt-button1"]').click()
			except Exception as e:
				pass
			
			# try:
			# 	# print(driver.find_element_by_xpath('//*[@id="defTsrDiv"]/div/div/div').text)
			# 	pass
			# except Exception as e:
			# 	pass

			#scrolls down to courses part
			driver.execute_script("window.scrollTo(0, 500)")
			
			field_links = []
			
			#gets rid of cookies pop up
			try:
				driver.find_element_by_xpath('//*[@id="cookieins"]/a').click()
			except Exception as e:
				pass

			for x in range(1,7):
				#clicks on a field
				driver.find_element_by_xpath('//*[@id="course"]/div/div[2]/div/div/div[' + str(x) + ']/div/div[3]/div/span[2]/a').click()
				
				for z in range(2,10):
					
					time.sleep(7)

					#creates a soup of the page
					page = driver.page_source
					soup = BeautifulSoup(page)
					field_page = driver.current_url
					#//*[@id="refineRst"]/div[3]/div/div[1]/ul/li[2]/a
					#//*[@id="refineRst"]/div[3]/div/div[1]/ul/li[2]/a
					#//*[@id="refineRst"]/div[3]/div/div[1]/ul/li[3]/a
					card_pairs = soup.find_all('div', {'class':"sr_set"})
					print(len(card_pairs))
					
					y = 0
					
					with open('hotCo_sheet1.csv', 'a') as writeFile:
						
						for pair in card_pairs:
							driver.execute_script("window.scrollTo(0, " + str(y * 130) + ")")
							cards = pair.find_all('div',{'class':"pr_rslt sr nrmtab"})
							
							for card in cards:
								
								name = card.find_all('h3')[0].text
								course_names.append(name)
								# print(name)
								
								duration = card.find_all('p')[1].text
								durations.append(duration)
								# print(duration)

								try:
									tuition = card.find_all('p')[3].text
								except Exception as e:
									tuition = ''
								tuition_fees.append(tuition)
								# print(tuition)
								
								#clicks to enter course card
								#//*[@id="8"]/div/div[1]/h3/a
								#//*[@id="9"]/div/div[1]/h3/a
								driver.find_element_by_xpath('//*[@id="' + str(y) + '"]/div/div[1]/h3/a').click()
								try:
									course_desc = driver.find_element_by_xpath('//*[@id="content"]/div[2]/div[1]/div/div[2]/div/p[2]').text
																		   
								except Exception as e:
									pass
								try:
									course_desc = driver.find_element_by_xpath('//*[@id="content"]/div[2]/div[1]/div/div[2]/div/p').text
								except Exception as e:
									pass
								descriptions.append(course_desc)
								# print(course_desc)
								
								csv_row = [uni_name, course_names[-1], descriptions[-1], durations[-1],tuition_fees[-1]]
								writer = csv.writer(writeFile)
								writer.writerow(csv_row)
								#to enter course card
								y = y + 1

								#gets back to courses in field page
								driver.get(field_page)
								time.sleep(5)
						try:
							driver.find_element_by_xpath('//*[@id="refineRst"]/div[3]/div/div['+str(z-1)+']/ul/li[' + str(z) + ']/a').click()
	
						except Exception as e:
							break

				#clicks back to uni page
				driver.find_element_by_xpath('//*[@id="cdBannerWrapId"]/div[1]/ul/li[5]/span/a').click()
				#scrolls down to courses part
				driver.execute_script("window.scrollTo(0, 900)")

			print('uni done')

	readFile.close()
driver.close()

#https://www.hotcoursesabroad.com/india/provider-result.html?catCode=H-2&collegeId=413900&countryid=32#search&catCode=H-2&collegeId=413900&countryid=32&provCntryId=32&restRefineFlag=Y&pageNo=1&provCntryId=32
#https://www.hotcoursesabroad.com/india/provider-result.html?catCode=H-2&collegeId=413900&countryid=32#search&catCode=H-2&collegeId=413900&countryid=32&provCntryId=32&restRefineFlag=Y&provCntryId=32&pageNo=2&provCntryId=32
