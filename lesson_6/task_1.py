from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 45, 0.1)

try:
    driver.get("http://uitestingplayground.com/ajax")
    driver.find_element(By.CSS_SELECTOR, "button.btn-primary").click()
    green_box = wait.until(EC.visibility_of_element_located(
    (By.CSS_SELECTOR, "bg-success"))).text
    text = green_box
    print(text)
except Exception as ex:
    print(ex)
finally:
    driver.quit()