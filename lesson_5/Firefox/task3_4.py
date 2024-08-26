from time import sleep
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


driver = webdriver.Firefox()
driver.get("http://the-internet.herokuapp.com/entry_ad")
wait = WebDriverWait(driver, 10)
modal_window = wait.until(
    EC.visibility_of_element_located((By.CSS_SELECTOR,".modal"))
)
close_button = wait.until(EC.element_to_be_clickable(
    (By.CSS_SELECTOR, ".modal-footer")
))
sleep(3)
driver.quit()