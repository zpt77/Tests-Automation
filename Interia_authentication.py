from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(r'C:\Users\tzubr\chromedriver')
driver.get("https://poczta.interia.pl/logowanie/")

#accept cookies
driver.find_element_by_class_name('rodo-popup-agree').click()

#create account
driver.find_element_by_xpath('//*[@id="sitebar"]/form/a').click()

#select free type of account
driver.find_element_by_xpath('//*[@id="mainApp"]/div/div/div/div/div[2]/div/div/div[1]/a/button').click()


#REGISTRATION FORM
name = driver.find_element_by_xpath('//form/div[1]/div[1]/input')
name.send_keys("imievbn")

surname = driver.find_element_by_xpath('//form/div[1]/div[2]/input')
surname.send_keys("nazwiskovbn")

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
mail_address.clear()
mail_address.send_keys('testowymail123vbn')

password = ",/T\w9PAy"

input_password = driver.find_element_by_name('password')
input_password.send_keys(password)

input_repassword = driver.find_element_by_name('rePassword')
input_repassword.send_keys(password)

accept_rules = driver.find_element_by_class_name('checkbox-label')
accept_rules.click()

driver.maximize_window()

create_account = driver.find_element_by_xpath('//*[@id="mainApp"]/div/div/div/div/div[2]/div/form/div[2]/button')
create_account.click()

#print(driver.find_element_by_xpath('//*[@id="mainApp"]/div/div/div/div/div[2]/div/form/div[2]/button').text)
