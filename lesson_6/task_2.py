from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("http://uitestingplayground.com/textinput")

input_field = driver.find_element(By.CSS_SELECTOR, "input#newButtonName")
input_field.send_keys("SkyPro")
button = driver.find_element(By.CSS_SELECTOR, "button.btn-primary")
button.click()
new_button_text = button.text
print(new_button_text)

driver.quit()