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

overviews = []
attributes = []
values = []

with open('uni_links.csv', 'r') as readFile:
	reader = csv.reader(readFile)
	for row in reader:
		with open('shiksha_sheet_2.csv', 'a') as writeFile:
			name = row[0]
			link = row[2]
			if link not in csv_headings:
				writer = csv.writer(writeFile)
				driver.get(str(link))
				try:
					overview = driver.find_element_by_xpath('//*[@id="main-wrapper"]/div[3]/div[2]/div/div[3]/div[1]/div[1]/div/div[2]').text
				except Exception as e:
					overview = ''
					pass

				table = driver.find_element_by_xpath('//*[@id="main-wrapper"]/div[3]/div[2]/div/div[3]/div[1]/div[4]/div[2]/div/div/table/tbody')
				rows = table.find_elements_by_tag_name('tr')

				overviews.append(overview)
				flag = 0
				for row in rows:
					cols = row.find_elements_by_tag_name('td')
					attributes.append(cols[0].text)
					values.append(cols[1].text)
					if flag == 0:
						csv_rows = [name, overviews[-1], attributes[-1], values[-1]]
					else:
						csv_rows = ['', '', attributes[-1], values[-1]]
					writer.writerow(csv_rows)
					flag = 1
				
			writeFile.close()
	readFile.close()
driver.close()
# rows = zip(course_names)

# with open('shiksha_scrapped.csv','a') as writeFile:
# 	writer = csv.writer(writeFile)
# 	for row in rows:
# 		writer.writerow(row)

