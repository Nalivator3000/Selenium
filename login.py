import time
import pickle
from selenium import webdriver


browser = webdriver.Firefox()

option = webdriver.FirefoxOptions()
option.set_preference('dom.webdriver.enabled', False)

option.set_preference('dom.notifications.enabled', False)
option.set_preference('media.volume_scale', '0.0')

try:
    # browser.delete_all_cookies()
    for cookie in pickle.load(open('session', 'rb')):
        browser.add_cookie(cookie)

    browser.get('https://facebook.com')

except:
    browser.get('https://facebook.com')

    time.sleep(3)

    form_xpath = '/html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[1]/div[1]/input'
    browser.find_element('xpath', form_xpath).send_keys('email')

    time.sleep(3)

    form_id = 'pass'
    browser.find_element('id', form_id).send_keys('password')

    time.sleep(3)

    finish_button_xpath = '/html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[2]/button'
    browser.find_element('xpath', finish_button_xpath).click()

    time.sleep(3)
    try:
        from_css = 'div.g4qalytl:nth-child(1) > div:nth-child(1) > div:nth-child(1)'
        browser.find_element('css selector', from_css).click()
    except:
        print('Cookies are already saved')

    pickle.dump(browser.get_cookie('facebook'), open('session', 'wb'))
