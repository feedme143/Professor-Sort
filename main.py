from selenium import webdriver
import json
import math

#def getJSON():
DRIVER_PATH = '/Users/Andrew_Hu/Desktop/chromedriver'
profs = []

driver = webdriver.Chrome(executable_path=DRIVER_PATH)

for i in range(166):
    string = "https://www.ratemyprofessors.com/filter/professor/?&page="+str(i+1)+"&filter=teacherlastname_sort_s+asc&query=*%3A*&queryoption=TEACHER&queryBy=schoolId&sid=124"

    driver.get(string)
    text = driver.find_element_by_xpath("/html/body/pre").text
    j = json.loads(text)
    profs +=j["professors"]

print(profs)