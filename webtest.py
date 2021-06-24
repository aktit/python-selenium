import time
from selenium.webdriver import Firefox
from selenium.webdriver.common.keys import Keys

import pandas
var1 = pandas.read_csv('data.csv')
questions = var1['Questions']
pub_date = var1['Pub_date']
res = dict(zip(questions, pub_date))

for i,j in res.items():
    browser = Firefox()
    browser.get('http://localhost:8000/admin')
    search_form1 = browser.find_element_by_name('username')
    search_form1.send_keys('apple')
    search_form2 = browser.find_element_by_name('password')
    search_form2.send_keys('123456')
    search_form1.send_keys(Keys.ENTER)
    time.sleep(1)

    click_add = browser.find_element_by_xpath('//*[@id="content-main"]/div[3]/table/tbody/tr/td[1]/a')
    click_add.click()
    question = browser.find_element_by_name('question_text')
    question.send_keys(i)
    date = browser.find_element_by_name('pub_date')
    date.send_keys(j)
    click_save = browser.find_element_by_name('_save')
    click_save.click()
    time.sleep(1)
    browser.close()

