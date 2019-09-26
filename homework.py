import os
import sys
import pandas as pd

from selenium import webdriver
from time import sleep

sleeptime = 5
assignment_name = sys.argv[1]

# import grade from csv file
data = pd.read_csv("/Users/tedyap/Desktop/CS125/Fall-2019/" + assignment_name + "/" + assignment_name + "/grades.csv")
student = data["name"].tolist()
grade = data["grade"].tolist()

driver = webdriver.Chrome("/usr/local/bin/chromedriver")
driver.get("https://courses.iwu.edu/mod/assign/view.php?id=271976&action=grader")

submit = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/section/div/div/div/div[1]/a")
submit.click()

# login 
username = driver.find_element_by_id("username")
username.send_keys("username")

password = driver.find_element_by_id("password")
password.send_keys("password")

submit = driver.find_element_by_xpath("/html/body/div/div/div/div/form/section[3]/input[4]")
submit.click()

for i in range(len(student)):
	sleep(sleeptime)
	name = driver.find_element_by_xpath("//*/em[1]/small")
	index = student.index(name.text)

	# enter grade	
	grade_box = driver.find_element_by_xpath('//*[@id="id_grade"]')
	grade_box.send_keys(grade[index])

	sleep(sleeptime)
	element = driver.find_element_by_xpath('//*[@title="Add..."]')
	element.click()

	# upload feedback files
	sleep(sleeptime)
	element = driver.find_element_by_xpath('//*[@name="repo_upload_file"]')
	file_name = os.listdir("/Users/tedyap/Desktop/CS125/Fall-2019/" + assignment_name + "/" + assignment_name + "/" + name.text + "/")[0]
	element.send_keys("/Users/tedyap/Desktop/CS125/Fall-2019/" + assignment_name + "/" + assignment_name + "/" + name.text + "/" + file_name + "/" + assignment_name + ".ipynb.pdf")

	sleep(sleeptime)
	element = driver.find_element_by_xpath('//*[@class="fp-upload-btn btn-primary btn"]')
	element.click()

	# save and go to next student
	sleep(sleeptime)
	save = driver.find_element_by_xpath('//*[@name="saveandshownext"]')
	save.click()

	sleep(sleeptime)
	ok = driver.find_element_by_xpath('//*[@value="Ok"]')
	ok.click()







