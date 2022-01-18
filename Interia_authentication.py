import time

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException


driver = webdriver.Chrome(r'C:\Users\tzubr\chromedriver')
login_page = "https://poczta.interia.pl/logowanie/"
driver.get(login_page)

driver.find_element_by_class_name('rodo-popup-agree').click()

#create account
driver.find_element_by_xpath('//*[@id="sitebar"]/form/a').click()

#select free type of account
driver.find_element_by_xpath('//*[@id="mainApp"]/div/div/div/div/div[2]/div/div/div[1]/a/button').click()


#REGISTRATION FORM

name = driver.find_element_by_xpath('//form/div[1]/div[1]/input')
name.send_keys("namexdqv")

surname = driver.find_element_by_xpath('//form/div[1]/div[2]/input')
surname.send_keys("surnamexcv")

day_of_birth = driver.find_element_by_xpath('//form/div[1]/div[3]/div[1]/input')
day_of_birth.send_keys("01")

month_of_birth = driver.find_element_by_xpath('//form/div[1]/div[3]/div[2]/div[1]')
month_of_birth.click()
driver.find_element_by_tag_name('li').click()

year_of_birth = driver.find_element_by_xpath('//form/div[1]/div[3]/div[3]/input')
year_of_birth.send_keys("2000")

sex = driver.find_element_by_xpath('//form/div[1]/div[4]/div[1]')
sex.click()
driver.find_element_by_xpath('//form/div[1]/div[4]/ul/li[1]').click()

mail_address = driver.find_element_by_xpath('//form/div[1]/div[5]/div[1]/input')
mail_address.click()

password = ",/T\w9PAy"

input_password = driver.find_element_by_name('password')
input_password.send_keys(password)

input_repassword = driver.find_element_by_name('rePassword')
input_repassword.send_keys(password)

accept_rules = driver.find_element_by_class_name('checkbox-label')
accept_rules.click()

driver.maximize_window()

time.sleep(2)

create_btn = driver.find_element_by_xpath('//*[@id="mainApp"]/div/div/div/div/div[2]/div/form/div[2]/button')
create_btn.click()

#get full mail address

#solving ended session

timeout = 8
time.sleep(5)
try:
    driver.find_element_by_xpath('//*[@id="pass"]').send_keys(password)
    driver.find_element_by_id('formSubmit').click()
    timeout = 15
except NoSuchElementException:
    print("extra action wasn't needed")

try:
    WebDriverWait(driver,timeout).until(EC.presence_of_element_located((By.XPATH,'//*[@id="wrapper"]/section[4]/div/div/div[1]/div/div/div'))).click()
    mail_address = driver.find_element_by_xpath('//*[@id="wrapper"]/section[4]/div/div[1]/div[2]/div/div[4]').text
except TimeoutException:
    print("Timeout") 

driver.close()


#failed login
driver = webdriver.Chrome(r'C:\Users\tzubr\chromedriver')
driver.get(login_page)

driver.find_element_by_class_name('rodo-popup-agree').click()
login_mail = driver.find_element_by_id('email')
login_mail.send_keys(mail_address)

login_password = driver.find_element_by_id('password')
login_password.send_keys("wrongpass")

driver.find_element_by_xpath('//*[@id="sitebar"]/form/button').click()

time.sleep(2)
driver.close()

#succesful login
driver = webdriver.Chrome(r'C:\Users\tzubr\chromedriver')
driver.get(login_page)

driver.find_element_by_class_name('rodo-popup-agree').click()

login_mail = driver.find_element_by_id('email')
login_mail.send_keys(mail_address)

login_password = driver.find_element_by_id('password')
login_password.send_keys(password)

driver.find_element_by_xpath('//*[@id="sitebar"]/form/button').click()

#get first mail title

timeout = 3
try:
    mailbox = WebDriverWait(driver,timeout).until(EC.presence_of_element_located((By.CLASS_NAME,'msglist-item__message__subject-text')))
    print(mailbox.text)
except TimeoutException:
    print("Timeout") 
