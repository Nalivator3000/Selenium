from selenium import webdriver


user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)' \
             ' AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'

option = webdriver.FirefoxOptions()
option.set_preference('dom.webdriver.enabled', False)
option.set_preference('general.useragent.override', user_agent)
browser = webdriver.Firefox(options=option)
browser.get('https://wtools.io/ru/check-my-user-agent')
