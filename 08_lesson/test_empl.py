import pytest
import requests
import json
from 08_lesson.employ import Employer, Company
from 08_lesson.constanse import URL

employer = Employer()
company = Company()

def test_get_auth_token(get_token: json.Any):
    token = get_token
    assert token is not None
    assert isinstance(token, str)
    
def test_get_company_id():
    company_id = company.last_active_company_id()
    assert company_id is not None
    assert str(company_id).isdigit()

def test_add_employer(get_token: json.Any):
    token = str(get_token)
    company_id = company.last_active_company_id()
    body_employer = {
        'id': 0,
        'firstName': 'Frodo',
        'lastName': 'Baggince',
        'middleName': 'string',
        'companyId': company_id,
        'url': 'string',
        'phone': '+1 (555) 555-5555',
        'birthdate': '1888-11-11',
        'isActive': 'true'
    }
    new_employer_id = (employer.add.new(token, body_employer))['id']
    assert new_employer_id is not None
    assert str(new_employer_id).isdigit()

    info = employer.get_info(new_employer_id)
    assert info.json()['id'] == new_employer_id
    assert info.status_code == 200

def test_create_employee_missing_fields(get_token):
    token = str(get_token)
    company_id = company.last_active_company_id()
    body_employer = {
        'firstName': 'Frodo',
        'lastName': 'Baggince',
        'companyId': company_id,
        'url': 'string',
        'isActive': 'true'
    }
    new_employer = (employer.add.new(token, body_employer))['id']
    assert new_employer['message'] == 'Internal server error'
   
    def test_add_employer_without_token():
        company_id = company.last_active_company_id()
        token = ""
        body_employer = {
        'id': 0,
        'firstName': 'Frodo',
        'lastName': 'Baggince',
        'middleName': 'string',
        'companyId': company_id,
        'url': 'string',
        'phone': '+1 (555) 555-5555',
        'birthdate': '1888-11-11',
        'isActive': 'true'
    }
    new_employer = employer.add_new(token, body_employer)
    assert new_employer['message'] == 'Unauthorized'


 




   

   