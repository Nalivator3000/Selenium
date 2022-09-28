import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


browser = webdriver.Firefox()
browser.get('https://youtube.com')
html = browser.find_element('tag name', 'html')

for i in range(1000):
    html.send_keys(Keys.DOWN)
    time.sleep(0.01)
