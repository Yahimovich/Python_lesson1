from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
try:
    driver.get('http://the-internet.herokuapp.com/login')
    username_input = driver.find_element(By.NAME, 'username')
    password_input = driver.find_element(By.NAME, 'password')
    username_input.send_keys('tomsmith')
    password_input.send_keys('SuperSecretPassword!')
    login_button = driver.find_element(By.TAG_NAME, 'button')
    login_button.click()
    time.sleep(5)
finally:
    driver.quit()


