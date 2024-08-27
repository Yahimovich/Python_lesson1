import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
@pytest.fixture

def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_slow_calculator(driver):
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    
    delay_input = driver.find_element(By.CSS_SELECTOR, "#delay")
    delay_input.clear()
    delay_input.send_keys("45")

    button_7 = driver.find_element(By.XPATH, "//span[text() = '7']")
    button_7.click()

    button_plus = driver.find_element(By.XPATH, "//span[text() = '+']")
    button_plus.click()

    button_8 = driver.find_element(By.XPATH, "//span[text() = '8']")
    button_8.click()

    button_equals = driver.find_element(By.XPATH, "//span[text() = '=']")
    button_equals.click()

    wait = WebDriverWait(driver, 50)

    result_display = wait.until(EC.text_to_be_present_in_element(
        (By.CSS_SELECTOR, "div.screen"), "15"))
    
    result_text = driver.find_element(By.CSS_SELECTOR, "div.screen").text
    
    assert result_text == "15"