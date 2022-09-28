import time
from selenium import webdriver


browser = webdriver.Firefox()

option = webdriver.FirefoxOptions()
option.set_preference('dom.webdriver.enabled', False)

option.set_preference('dom.notifications.enabled', False)
option.set_preference('media.volume_scale', '0.0')

browser.get('https://www.facebook.com/')

time.sleep(2)

next_button_xpath = '/html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[5]/a'
browser.find_element('xpath', next_button_xpath).click()

time.sleep(2)

# form_xpath = '/html/body/div[5]/div[2]/div/div/div[2]/div/div/div[1]/form/div[1]/div[1]/div[1]/div[1]/div/input'
# browser.find_element('xpath', form_xpath).send_keys('Виктория')

form_js = '#u_2_b_bj'
browser.find_element('css selector', form_js).send_keys('Виктория')

time.sleep(5)

form_xpath = '/html/body/div[6]/div[2]/div/div/div[2]/div/div/div[1]/form/div[1]/div[1]/div[1]/div[2]/div/div[1]/input'
browser.find_element('xpath', form_xpath).send_keys('Мальцева')

time.sleep(5)

form_xpath = '/html/body/div[6]/div[2]/div/div/div[2]/div/div/div[1]/form/div[1]/div[2]/div/div[1]/input'
browser.find_element('xpath', form_xpath).send_keys('380661231212')

time.sleep(5)

form_xpath = '/html/body/div[6]/div[2]/div/div/div[2]/div/div/div[1]/form/div[1]/div[4]/div/div[1]/input'
browser.find_element('xpath', form_xpath).send_keys('Gjs%^jsd123bg')

time.sleep(5)

form_xpath = '/html/body/div[6]/div[2]/div/div/div[2]/div/div/div[1]/form/div[1]/div[5]/div[2]/span/span/select[1]'
browser.find_element('xpath', form_xpath).send_keys('5')

time.sleep(5)

form_xpath = '/html/body/div[6]/div[2]/div/div/div[2]/div/div/div[1]/form/div[1]/div[5]/div[2]/span/span/select[2]'
browser.find_element('xpath', form_xpath).send_keys('8')

time.sleep(5)

form_xpath = '/html/body/div[6]/div[2]/div/div/div[2]/div/div/div[1]/form/div[1]/div[5]/div[2]/span/span/select[3]'
browser.find_element('xpath', form_xpath).send_keys('1994')

time.sleep(5)

form_xpath = '/html/body/div[6]/div[2]/div/div/div[2]/div/div/div[1]/form/div[1]/div[7]/span/span[1]/input'
browser.find_element('xpath', next_button_xpath).click()

time.sleep(5)

next_button_xpath = '/html/body/div[6]/div[2]/div/div/div[2]/div/div/div[1]/form/div[1]/div[11]/button'
browser.find_element('xpath', next_button_xpath).click()


# /html/body/div[6]/div[2]/div/div/div[2]/div/div/div[1]/form/div[1]/div[1]/div[1]/div[1]/div/div[1]/input
# /html/body/div[5]/div[2]/div/div/div[2]/div/div/div[1]/form/div[1]/div[1]/div[1]/div[1]/div/input
# /html/body/div[5]/div[2]/div/div/div[2]/div/div/div[1]/form/div[1]/div[1]/div[1]/div[1]/div/input