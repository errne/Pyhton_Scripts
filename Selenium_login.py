import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()

driver.get("https://society6.com/")

cookie_button = driver.find_element(By.ID, "onetrust-accept-btn-handler")
cookie_button.click()
time.sleep(1)

login_button = driver.find_element_by_xpath('//*[@id="nav-login-trigger"]')
login_button.click()
time.sleep(1)

file = open("secrets.txt", "r")
user = file.readline()
passwords = file.readline()

username = driver.find_element_by_xpath('//*[@id="email"]')
username.send_keys(user)

password = driver.find_element_by_xpath('//*[@id="password"]')
password.send_keys(passwords)

driver.find_element_by_name("login").click()
