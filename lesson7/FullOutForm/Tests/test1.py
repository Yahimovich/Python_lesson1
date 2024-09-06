from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from lesson7.Pages.Datafields import DataField
from lesson7.Pages.Mainpage import MainPage
from lesson7.constans import Form_URL
from lesson7.Data_types.data import *

def test_assertion(chrome_browser):
    main_page = MainPage(chrome_browser)
    main_page.find_fields()
    main_page.filling_fields()
    main_page.click_submit_button()

    data_field = DataField(chrome_browser)
    data_field.find_fields()
    data_field.get_class_first_name()
    data_field.get_class_last_name()
    data_field.get_class_address()
    data_field.get_class_phone()
    data_field.get_class_city()
    data_field.get_class_city()
    data_field.get_class_country()
    data_field.get_class_job_position()
    data_field.get_class_company()
    data_field.get_class_zip_code()

    assert "succsess" in data_field.get_class_first_name()
    assert "succsess" in data_field.get_class_last_name()
    assert "succsess" in data_field.get_class_address()
    assert "succsess" in data_field.get_class_phone()
    assert "succsess" in data_field.get_class_city()
    assert "succsess" in data_field.get_class_country()
    assert "succsess" in data_field.get_class_job_position()
    assert "succsess" in data_field.get_class_company()
    assert "danger" in data_field.get_class_zip_code()