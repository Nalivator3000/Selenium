import time
from selenium import webdriver


option = webdriver.FirefoxOptions()
option.set_preference('dom.webdriver.enabled', False)

option.set_preference('dom.notifications.enabled', False)
option.set_preference('media.volume_scale', '0.0')

browser = webdriver.Firefox(options=option)
browser.get('https://youtube.com')
