from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://the-internet.herokuapp.com/inputs")
input_field = driver.find_element(By.TAG_NAME, "input")
input_field.send_keys("1000")
sleep(4)
input_field.clear()
sleep(4)
input_field.send_keys("999")
sleep(4)
driver.quit()

driver = webdriver.Firefox()
driver.get("http://the-internet.herokuapp.com/inputs")
input_field = driver.find_element(By.TAG_NAME, "input")
input_field.send_keys("1000")
sleep(4)
input_field.clear()
sleep(4)
input_field.send_keys("999")
sleep(4)
driver.quit()