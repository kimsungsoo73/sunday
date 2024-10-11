from bs4 import BeautifulSoup
import time
import pandas as pd
import numpy as np
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ['enable-logging'])
driver = webdriver.Chrome(options = options)

url = 'https://pages.coupang.com/p/27166'
driver = webdriver.Chrome()
driver.get(url)

time.sleep(3)
driver.execute_script('window.scrollTo(0, (document.body.scrollHeight)-2700);')
# u_cbox_list = driver.find_element(by=By.CLASS_NAME, value='u_box_list' )
comment = driver.find_elements(by=By.CLASS_NAME, value='u_cbox_comment')

for i in range(6):
    u_cbox_nick = comment[i].find_element(by=By.CLASS_NAME, value='u_cbox_nick').text
    u_cbox_contents = comment[i].find_element(by=By.CLASS_NAME, value='u_cbox_contents').text
    u_cbox_date = comment[i].find_element(by=By.CLASS_NAME, value='u_cbox_date').text
    u_cbox_cnt_recomm = comment[i].find_element(by=By.CLASS_NAME, value='u_cbox_cnt_recomm').text
    print(u_cbox_nick, '\t', u_cbox_contents, '\t', u_cbox_date, '\t', u_cbox_cnt_recomm)

driver.implicitly_wait(10)
driver.close()

