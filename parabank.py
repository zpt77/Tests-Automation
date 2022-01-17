from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(r'C:\Users\tzubr\chromedriver')
driver.get("https://parabank.parasoft.com/parabank/index.htm")

login = "john"
password = "1234"

driver.find_element_by_name('username').send_keys(login)
driver.find_element_by_name('password').send_keys(password)
driver.find_element_by_xpath('//*[@id="loginPanel"]/form/div[3]/input').click()

result = driver.find_element_by_xpath('//*[@id="leftPanel"]/p').text
print(result)

if (result=="Welcome John Smith"):
	print("Test passed!")
else:
    print("Test failed")

