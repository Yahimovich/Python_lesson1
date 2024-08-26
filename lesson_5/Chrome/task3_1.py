from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()
driver.get("http://the-internet.herokuapp.com/add_remove_elements/")
for _ in range(5):
    add_button = driver.find_element(
        By.XPATH, "//button[text()='Add Element']").click()
    delete_button = driver.find_elements(
        "xpath", "//button[text()='Delete']"
    )
sleep(4)
print(f"Количество кнопок 'Delete': {len(delete_button)}")
driver.quit()

