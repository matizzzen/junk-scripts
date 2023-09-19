from selenium import webdriver
from selenium.webdriver.common.by import By
import time

url = r'https://mail.anteystroy.ru/owa'
login = r'corp\a.ma'
pwd = r'Kabachok12!'

options = webdriver.EdgeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Edge(options=options)
driver.get(url)

print(driver.title)
