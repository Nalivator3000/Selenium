from selenium import webdriver


option = webdriver.FirefoxOptions()
option.headless = True

browser = webdriver.Firefox(options=option)
browser.get('https://mynickname.com/generate')

while True:
    refresh_xpath = '/html/body/div[1]/div[1]/div[1]/div[2]/form/table/tbody/tr[5]/td[2]/input'
    browser.find_element('xpath', refresh_xpath).click()

    nickname = browser.find_element('id', 'register').get_attribute('href')[37:]
    print(f'Nickname: {nickname}')

