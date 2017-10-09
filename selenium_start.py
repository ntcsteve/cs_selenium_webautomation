import time
from selenium import webdriver

# Optional argument, add path to find your webdriver
driver = webdriver.Chrome()
driver.get('http://www.google.com/xhtml')

# Pause for 5s
time.sleep(5)

# Find the name of the element called q and enter 'ChromeDriver' into the textbox
search_box = driver.find_element_by_name('q')
search_box.send_keys('ChromeDriver')
search_box.submit()

# Pause for 5s
time.sleep(5)
driver.quit()
