from selenium import webdriver
import requests
from bs4 import BeautifulSoup

driver = webdriver.Chrome('chromedriver.exe')
url = 'https://ko.dict.naver.com/#/search?query=고혈압'
driver.get(url)

url= 'https://ko.dict.naver.com/#/entry/koko/2e1028a367aa4b84b3c5478cfcfe2160'
response = requests.get(url)
response.raise_for_status()
html = response.text
soup = BeautifulSoup(html, 'html.parser')


driver.find_element_by_xpath('/html') #xpath 로 접근
print(soup)