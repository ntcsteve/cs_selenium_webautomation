import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select

# Optional argument, add path to find your webdriver
driver = webdriver.Chrome()

# letskodeit is a great practice site for selenium
driver.get('https://letskodeit.teachable.com/p/practice')

# example 1 - find and click the radio button for BMW
radio_BMW = driver.find_element_by_id("bmwradio")
radio_BMW.click()
time.sleep(4)

# example 2 - find and click the select button for Honda
select_Honda = Select(driver.find_element_by_id("carselect"))
select_Honda.select_by_value("honda")
time.sleep(4)

# example 3 - find and click the select button for Orange
multiple_select = Select(driver.find_element_by_id("multiple-select-example"))
multiple_select.select_by_value("orange")
time.sleep(4)

# example 4 - find and click the checkbox for Honda
checkbox_Honda = driver.find_element_by_id("hondacheck")
checkbox_Honda.click()
time.sleep(4)

# example 5 - find and enter the value 'Mercedes' into the textbox
enter_name = driver.find_element_by_id("name")
enter_name.send_keys("Mercedes")
time.sleep(4)

# example 6 - hover the mouse to expand the dropdown list and click 'reload'
driver.execute_script("window.scrollBy(0, 600);")
mouse_hover = driver.find_element_by_id("mousehover")
actions = ActionChains(driver)
actions.move_to_element(mouse_hover).perform()
time.sleep(4)

reload_link = driver.find_element_by_xpath("//div[@class='mouse-hover-content']//a[text()='Reload']")
actions.move_to_element(reload_link).click().perform()
print("Reloading the page")
time.sleep(4)

# example 7 - find the right iframe and enter 'Python for life!' into the textbox
driver.switch_to.frame("courses-iframe")
print("Switching to iframe")

iframe_textbox = driver.find_element_by_id("search-courses")
iframe_textbox.send_keys("Python for life!")
driver.switch_to.default_content()
print("Coming out from iframe")
time.sleep(4)

time.sleep(4)
driver.quit()
