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

def test_form_submission(driver):
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
    
    first_name = driver.find_element(By.NAME, "first-name")
    first_name.send_keys("Иван")

    last_name = driver.find_element(By.NAME, "last-name")
    last_name.send_keys("Петров")

    address = driver.find_element(By.NAME, "address")
    address.send_keys("Ленина, 55-3")

    email = driver.find_element(By.NAME, "e-mail")
    email.send_keys("test@skypro.com")

    phone_number = driver.find_element(By.NAME, "phone")
    phone_number.send_keys("+7985899998787")

    zip_code = driver.find_element(By.NAME, "zip-code")
    zip_code.send_keys("")

    city = driver.find_element(By.NAME, "city")
    city.send_keys("Москва")

    country = driver.find_element(By.NAME, "country")
    country.send_keys("Россия")

    job_position = driver.find_element(By.NAME, "job-position")
    job_position.send_keys("QA")

    company = driver.find_element(By.NAME, "company")
    company.send_keys("SkyPro")

    submit_button = driver.find_element(By.TAG_NAME, "submit")
    
    wait = WebDriverWait(driver, 40, 0.1)

    submit_button = wait.until(EC.element_to_be_clickable(
        (By.TAG_NAME, "button")))
    submit_button.click()

    zip_code_field = wait.until(EC.presence_of_element_located(
        (By.ID, "zip-code")))
    
    assert "danger" in zip_code_field.get_attribute("class")
    
    fields = ["first-name", "last-name", "address", "e-mail", "phone", "city", "country", "job-position", "company"]
    for field in fields:
        field_element = driver.find_element(By.ID, field)
        
        assert "success" in field_element.get_attribute("class")