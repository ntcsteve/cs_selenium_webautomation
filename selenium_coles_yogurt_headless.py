import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Headless Chrome example
# Optional argument, add path to find your webdriver
chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.get('https://www.coles.com.au')

# step 1 : find the search bar and enter my favourite yogurt description
search_bar = driver.find_element_by_id("ctl19_ctl02_txtSearch")

if search_bar is not None:
    print("Headless : Found the search bar")
    search_bar.send_keys("Berry Punnet Yoghurt 6 pack")
    time.sleep(4)

# step 2 : find my favourite yogurt
search_icon = driver.find_element_by_id("ctl19_ctl02_btnButtonSearch")

if search_icon is not None:
    print("Headless : Found the search icon")
    search_icon.click()
    time.sleep(4)

# step 3 : select my favourite yogurt
driver.execute_script("window.scrollBy(0, 600);")
confirmation = driver.find_element_by_class_name("button-main-inner")
if confirmation is not None:
    print("Headless : Found the confirmation button")
    confirmation.click()
    time.sleep(4)

# step 4 : sign in to order my favourite yogurt
login = driver.find_element_by_class_name("login")

if login is not None:
    print("Headless : Found the login button")
    login.click()

driver.close()
