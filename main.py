#! C:\Users\Rik\Desktop\wikipedia_scraper\wikipedia_scraper\Scripts\python.exe
import requests
from bs4 import BeautifulSoup
import pandas as pd
import re


print('script starten')


# # call the get method of requests on our specifications
# response = requests.get(f"{root_url}/{endpoint}", params=params)
# json_data = response.json()
# print(json_data)

root_url = 'https://country-leaders.onrender.com'

#Generate a Cookie
cookie = requests.get(f'{root_url}/cookie/')
cookie_response = cookie.json()
print(cookie_response)

#prepare the Cookie in a dictionary with the .cookies functionality of requests
cookies = {'user_cookie': cookie.cookies['user_cookie']}

#Validate the Cookie
cookie_val = requests.get(f'{root_url}/check/', cookies=cookies)
cookie_check = cookie_val.json()
print(cookie_check)

#Get the list of countries
country_list = requests.get(f'{root_url}/countries/', cookies=cookies) 
country_list_response = country_list.json()
print(country_list_response)
print(country_list_response[0])
#soup = BeautifulSoup(page.text, 'lxml')