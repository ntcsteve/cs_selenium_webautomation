import time
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# default timeout value
timeout = 4

# Headless Chrome with with presence of element located example
# Optional argument, add path to find your webdriver
chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.get('https://www.coles.com.au')

# webdriver short code
wait = WebDriverWait(driver, timeout,)

# example 1 - telling selenium to wait patiently for 4s
print("Example 1 =", time.strftime("%H:%M:%S"))
time.sleep(4)
print("Example 1 =", time.strftime("%H:%M:%S"))
catalogue1 = driver.find_element_by_class_name('catalogue-specials')

if catalogue1 is not None:
    print("Found the right link for Catalogues & specials")
    catalogue1.click()
    print("Using time.sleep")
else:
    print("Can't find the right link for Catalogues & specials")

# example 2 - using a timeout value to wait patiently for 4s
print("Example 2 =", time.strftime("%H:%M:%S"))
catalogue2 = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'catalogue-specials')))
print("Example 2 =", time.strftime("%H:%M:%S"))

if catalogue2 is not None:
    print("Found the right link for Catalogues & specials")
    catalogue2.click()
    print("Using EC and element located")
else:
    print("Can't find the right link for Catalogues & specials")

driver.quit()
