from selenium import webdriver


browser = webdriver.Firefox()
browser.get('https://facebook.com')
browser.save_screenshot('screen1.png')
browser.refresh()
browser.quit()