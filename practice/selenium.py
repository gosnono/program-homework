from selenium import webdriver
import time
import os
from urlib.request import urlopen

browser = webdriver.Chrome()
url = "https://search.naver.com/search.naver?where=image&sm=tab_jum&query=%EA%B0%95%EC%95%84%EC%A7%80"
browser.get(url)


