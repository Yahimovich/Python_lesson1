import pytest
from selenium import webdriver

@pytest.fixture()
def chrome_browser():
    driver = webdriver_Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()