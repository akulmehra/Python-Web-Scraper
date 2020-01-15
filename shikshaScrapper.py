from bs4 import BeautifulSoup
import urllib.request
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.action_chains import ActionChains
import csv

driver = webdriver.Chrome('/Users/akulmehra/Desktop/leverage/chromedriver')
driver.implicitly_wait(30)
driver.maximize_window()

csv_headings = {'University Name', 'Link'}


course_names = []
durations = []
descriptions = []
tuition_fees = []
total_fees = []

with open('uni_links.csv', 'r') as readFile:
	reader = csv.reader(readFile)
	for row in reader:
		if row[2] not in csv_headings:
			# opens url
			driver.get(str(row[2]))

			# clicks on courses
			try:
				driver.find_element_by_xpath('//*[@id="main-wrapper"]/div[3]/div[2]/div/div[1]/div[2]/a[2]/label').click()
			except:
				pass
			try:
				driver.find_element_by_xpath('//*[@id="main-wrapper"]/div[3]/div[2]/div/div[1]/div[2]/a[2]')
			except:
				pass
						
			name = str(row[0])

			for x in range(0, 100):


				try:
					with open('shiksha_scrapped_test.csv','a') as writeFile:
						writer = csv.writer(writeFile)


						driver.execute_script("window.scrollTo(0, " + str(110 * (x+1)) + ")")
						# finds name of course
						course = driver.find_element_by_xpath('//*[@id="allC'+ str(x) + '"]/a')

						# appends to list of course names
						course_names.append(course.text)
						# clicks on view details
						driver.find_element_by_xpath('//*[@id="allC'+ str(x) + '"]/div/div[2]/a').click()
						# finds duration
						
						try:
							duration = driver.find_element_by_xpath('//*[@id="main-wrapper"]/div[3]/div[2]/div/div[3]/div[1]/div[2]/div[2]/div[1]/table/tbody/tr[1]/td[2]').text
							
						except Exception as e:
							pass

						try:
							duration = driver.find_element_by_xpath('//*[@id="main-wrapper"]/div[3]/div[2]/div/div[3]/div[1]/div[1]/div[2]/div[1]/table/tbody/tr[1]/td[2]').text
						except:
							pass		

						
						# finds course descriptions
						try:
							description = driver.find_element_by_xpath('//*[@id="main-wrapper"]/div[3]/div[2]/div/div[3]/div[1]/div[2]/div[2]/div[2]/div/ul').text
						except Exception as e:
							# print(e)
							pass
						try:
							description = driver.find_element_by_xpath('//*[@id="main-wrapper"]/div[3]/div[2]/div/div[3]/div[1]/div[2]/div[2]/div[2]/div/p').text
						except Exception as e:
							# print(e)
							pass
						try:						
							total_fee_table = driver.find_element_by_xpath('//*[@id="main-wrapper"]/div[3]/div[2]/div/div[3]/div[1]/div[3]/div[2]/div[2]/div[2]/table')
						except:
							pass
						try:
							total_fee_table = driver.find_element_by_xpath('//*[@id="main-wrapper"]/div[3]/div[2]/div/div[3]/div[1]/div[2]/div[2]/div[2]/div[2]/table')
						except:
							pass

						amount = total_fee_table.find_element_by_tag_name('strong').text
						try:
							tuition_fee = driver.find_element_by_xpath('//*[@id="main-wrapper"]/div[3]/div[2]/div/div[3]/div[1]/div[3]/div[2]/div[1]/div[2]/table/tbody/tr/td[2]').text
																	
						except Exception as e:
							pass

						try:
							tuition_fee = driver.find_element_by_xpath('//*[@id="main-wrapper"]/div[3]/div[2]/div/div[3]/div[1]/div[2]/div[2]/div[1]/div[2]/table/tbody/tr/td[2]').text
						except Exception as e:
							pass

						tuition_fees.append(tuition_fee)
						descriptions.append(description)
						total_fees.append(amount)
						# appends duration
						durations.append(duration)

						# brings back to courses
						driver.find_element_by_xpath('//*[@id="main-wrapper"]/div[3]/div[2]/div/div[1]/div[2]/a[2]/label').click()

						rows = [name, course_names[-1], durations[-1], descriptions[-1], tuition_fees[-1] , total_fees[-1]]

						
					# for row in rows:
						#print(rows)
						writer.writerow(rows)
						writeFile.close()
						print('course done')

				except Exception as e:
					print(e)
					break

					
			emptyRow = ['','','','','']
			with open('shiksha_scrapped_test.csv','a') as writeFile:
				writer = csv.writer(writeFile)
				writer.writerow(emptyRow)
				writeFile.close()			
			print('uni done')
				


		

	



driver.close()

#//*[@id="allC0"]/a
#//*[@id="allC1"]/a

#//*[@id="allC0"]/div/div[2]/a
#//*[@id="allC1"]/div/div[2]/a

#//*[@id="main-wrapper"]/div[3]/div[2]/div/div[3]/div[1]/div[2]/div[2]/div[1]/table/tbody/tr[1]/td[2]

#//*[@id="main-wrapper"]/div[3]/div[2]/div/div[3]/div[1]/div[2]/div[2]/div[1]/table/tbody/tr[1]/td[2]

#//*[@id="allC0"]
#//*[@id="allC1"]
#for row in reader:	
#if row[2] not in csv_headings:

# //*[@id="main-wrapper"]/div[3]/div[2]/div/div[3]/div[1]/div[2]/div[2]/div[2]/div/ul/li[1]
# //*[@id="main-wrapper"]/div[3]/div[2]/div/div[3]/div[1]/div[2]/div[2]/div[2]/div/ul/li[2]
# //*[@id="main-wrapper"]/div[3]/div[2]/div/div[3]/div[1]/div[2]/div[2]/div[2]/div/ul/li[1]

# //*[@id="main-wrapper"]/div[3]/div[2]/div/div[3]/div[1]/div[2]/div[2]/div[2]/div/p



#//*[@id="main-wrapper"]/div[3]/div[2]/div/div[3]/div[1]/div[3]/div[2]/div[2]/div[2]/table/tbody/tr[11]/td[2]/strong


