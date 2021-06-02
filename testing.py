import time
from selenium import webdriver

# browser = webdriver.Chrome('path/to/chromedriver')
# browser.get('http://localhost:5000')
# assert browser.title == 'Adventure Spark'

# email = browser.find_element_by_id('login-email')
# email.send_keys("admin@gmail.com")
# password = browser.find_element_by_id('login-password')
# password.send_keys("admin")

# btn = browser.find_element_by_id('login-button')
# btn.click()

# result = browser.find_element_by_id('result')
# assert result.text == "7"
# browser.close()

driver = webdriver.Chrome()  # Optional argument, if not specified will search path.
driver.get('http://www.google.com/');
time.sleep(5) # Let the user actually see something!
search_box = driver.find_element_by_name('q')
search_box.send_keys('ChromeDriver')
search_box.submit()
time.sleep(5) # Let the user actually see something!
driver.quit()