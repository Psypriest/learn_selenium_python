from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Launch the browser
driver = webdriver.Chrome()

# Navigate to a URL
driver.get("https://www.example.com")

# Find an element by ID
element = driver.find_element_by_id("myid")

# Find an element by name
element = driver.find_element_by_name("myname")

# Find an element by class name
element = driver.find_element_by_class_name("myclass")

# Find an element by CSS selector
element = driver.find_element_by_css_selector("myselector")

# Find an element by XPath
element = driver.find_element_by_xpath("mypath")

# Click an element
element.click()

# Enter text into an input field
element.send_keys("mytext")

# Submit a form
form = driver.find_element_by_tag_name("form")
form.submit()

# Get the current URL
url = driver.current_url

# Get the title of the current page
title = driver.title

# Get the source code of the current page
source_code = driver.page_source

# Wait for an element to appear
element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "myid"))
)

# Wait for an element to be clickable
element = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "myid"))
)

# Wait for an element to be visible
element = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, "myid"))
)

# Click a button with JavaScript
button = driver.find_element_by_id("mybutton")
driver.execute_script("arguments[0].click();", button)

# Find multiple elements by CSS selector
elements = driver.find_elements_by_css_selector("myselector")

# Switch to an iframe
iframe = driver.find_element_by_tag_name("iframe")
driver.switch_to.frame(iframe)

# Switch back to the main frame
driver.switch_to.default_content()

# Drag and drop an element
source_element = driver.find_element_by_id("source")
target_element = driver.find_element_by_id("target")
webdriver.ActionChains(driver).drag_and_drop(source_element, target_element).perform()

# Double-click an element
element = driver.find_element_by_id("myid")
webdriver.ActionChains(driver).double_click(element).perform()

# Right-click an element
element = driver.find_element_by_id("myid")
webdriver.ActionChains(driver).context_click(element).perform()

# Hover over an element
element = driver.find_element_by_id("myid")
webdriver.ActionChains(driver).move_to_element(element).perform()

# Scroll down the page
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

# Scroll up the page
driver.execute_script("window.scrollTo(0, 0);")

# Take a screenshot of the current page
driver.save_screenshot("screenshot.png")

# Resize the browser window
driver.set_window_size(800, 600)

# Maximize the browser window
driver.maximize_window()

# Refresh the page
driver.refresh()

# Close the browser
driver.quit()

# Get the text of an element
text = element.text

# Get the value of an input field
value = element.get_attribute("value")

# Clear the text of an input field
element.clear()

# Select an option from a drop-down list by value
select = driver.find_element_by_tag_name

# Find an element by link text
element = driver.find_element_by_link_text("mylinktext")

# Find an element by partial link text
element = driver.find_element_by_partial_link_text("mylinktext")

# Find an element by tag name
element = driver.find_element_by_tag_name("mytagname")

# Get the current window handle
current_window_handle = driver.current_window_handle

# Get all window handles
window_handles = driver.window_handles

# Switch to a window by handle
driver.switch_to.window(window_handle)

# Switch to the next window
driver.switch_to.window(driver.window_handles[-1])

# Switch to the previous window
driver.switch_to.window(driver.window_handles[-2])

# Close the current window
driver.close()

# Open a new window
driver.execute_script("window.open('https://www.example.com', 'new_window')")

# Get the alert text
alert_text = driver.switch_to.alert.text

# Accept an alert
driver.switch_to.alert.accept()

# Dismiss an alert
driver.switch_to.alert.dismiss()

# Get the value of a cookie
cookie_value = driver.get_cookie("mycookie")["value"]

# Set a cookie
cookie = {"name": "mycookie", "value": "myvalue"}
driver.add_cookie(cookie)

# Delete a cookie
driver.delete_cookie("mycookie")

# Delete all cookies
driver.delete_all_cookies()

# Get the current window position
window_position = driver.get_window_position()

# Set the window position
driver.set_window_position(0, 0)

# Get the current window size
window_size = driver.get_window_size()

# Set the window size
driver.set_window_size(800, 600)

# Get the attribute value of an element
attribute_value = element.get_attribute("myattribute")

# Get the CSS value of an element
css_value = element.value_of_css_property("mycssproperty")

# Move to an element
webdriver.ActionChains(driver).move_to_element(element).perform()

# Click and hold an element
webdriver.ActionChains(driver).click_and_hold(element).perform()

# Release a held element
webdriver.ActionChains(driver).release(element).perform()

# Drag and drop an element to a specified location
webdriver.ActionChains(driver).drag_and_drop_by_offset(element, x_offset, y_offset).perform()

# Execute JavaScript code
driver.execute_script("alert('hello world!');")

# Switch to an alert
alert = driver.switch_to.alert

# Switch to a frame by name or ID
driver.switch_to.frame("myframe")

# Switch to a frame by index
driver.switch_to.frame(0)

# Switch back to the default content
driver.switch_to.default_content()

# Switch to the parent frame
driver.switch_to.parent_frame()

# Wait for a page to load
driver.implicitly_wait(10)

# Navigate forward in the browser history
driver.forward()

# Navigate backward in the browser history
driver.back()

# Get the value of a hidden input field
value = driver.execute_script("return document.getElementById('myid').value;")

