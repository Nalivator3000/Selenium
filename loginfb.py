import time
from selenium import webdriver


browser = webdriver.Firefox()

option = webdriver.FirefoxOptions()
option.set_preference('dom.webdriver.enabled', False)

option.set_preference('dom.notifications.enabled', False)
option.set_preference('media.volume_scale', '0.0')

browser.get('https://www.facebook.com/')

time.sleep(5)

form_xpath = '/html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[1]/div[1]/input'
browser.find_element('xpath', form_xpath).send_keys('ihippi4@gmail.com')

time.sleep(5)

form_xpath = '/html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[1]/div[2]/div/input'
browser.find_element('xpath', form_xpath).send_keys('Fib112358132134')

time.sleep(5)

next_button_xpath = '/html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[2]/button'
browser.find_element('xpath', next_button_xpath).click()
