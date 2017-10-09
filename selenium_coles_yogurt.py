import time
from selenium import webdriver

# Optional argument, add path to find your webdriver
driver = webdriver.Chrome()
driver.get('https://www.coles.com.au')

# step 1 : find the search bar and enter my favourite yogurt description
search_bar = driver.find_element_by_id("ctl19_ctl02_txtSearch")
search_bar.send_keys("Berry Punnet Yoghurt 6 pack")
time.sleep(4)

# step 2 : find my favourite yogurt
search_icon = driver.find_element_by_id("ctl19_ctl02_btnButtonSearch")
search_icon.click()
time.sleep(4)

# step 3 : select my favourite yogurt
driver.execute_script("window.scrollBy(0, 600);")
confirmation = driver.find_element_by_class_name("button-main-inner")
confirmation.click()
time.sleep(4)

# step 4 : sign in to order my favourite yogurt
login = driver.find_element_by_class_name("login")
login.click()
time.sleep(4)

time.sleep(4)
driver.close()
