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

def test_purchase_items(driver):
    
    driver.get("https://www.saucedemo.com/")
    
    username = driver.find_element(By.ID, "user-name")
    username.send_keys("standard_user")

    password = driver.find_element(By.ID, "password")
    password.send_keys("secret_sauce")

    login_button = driver.find_element(By.ID, "login-button")
    login_button.click()

    backpack = driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
    backpack.click()

    bolt_t_shirt = driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
    bolt_t_shirt.click()

    onesie = driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie")
    onesie.click()

    cart_button = driver.find_element(By.CSS_SELECTOR, ".shopping_cart_link")
    cart_button.click()
    
    checkout_button = driver.find_element(By.ID, "checkout")
    checkout_button.click()
    
    first_name = driver.find_element(By.ID, "first-name")
    first_name.send_keys("Юлия")

    last_name = driver.find_element(By.ID, "last-name")
    last_name.send_keys("Яхимович")

    postal_code = driver.find_element(By.ID, "postal-code")
    postal_code.send_keys("660016")

    continue_button = driver.find_element(By.ID, "continue")
    continue_button.click()
    
    total_price = driver.find_element(By.CSS_SELECTOR, ".summary_total_label").text
    assert total_price == "Total: $58.29"