import json
import token
import requests
from 08_lesson.constanse import URL

path = '/employee/'

class Company:
    def _init_(self, url=URL):
        self.url = url

    def create(self, token: str, body: json):
        headers = {'x-client-token': token}
        response = requests.post(
            self.url + '/company', headers=headers, params=body)
        return response.json()
    
    def last_active_company_id(self):
        active_params = {'active': 'true'}
        response = requests.get(
            self_url + '/company', params=active_params)
        return response.json()[-1]['id']


class Employer:
    def __init__(self, url=URL):
        self.url = url

    def get_list(self, company_id: int):
        company = {'company': company_id}
        response = requests.get(
            self.url + '/employee', params=company)
        return response.json()
    
    def add_new(self, token: str, body: json):
        headers = {'x-client-token': token}
        response = requests.post(
            self.url + '/employee', headers=headers, json=body)
        return response.json()
    
    def get_info(self, employee_id: int):
        response = requests.get(self.url + path + str(employee_id))
        return response.json()

    def change_info(self, token: str, employee_id: int, body: json):
        headers = {'x-client-token': token}
        response = requests.patch(self.url + path + str(employee_id), headers=headers,
                                  json=body)
        return response.json()    

