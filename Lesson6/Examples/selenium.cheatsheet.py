"""
Selenium with Python Cheat Sheet

This cheat sheet provides an overview of the Selenium module in Python,
including common usage patterns and code examples.
"""

# Installation:
# Install Selenium using pip:
# pip install selenium
#
# Install webdriver-manager to automatically manage browser drivers:
# pip install webdriver-manager

# Importing Selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

# Initializing WebDriver

# For Chrome:
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Initialize Chrome WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Navigating to a URL
driver.get('https://www.example.com')

# Locating Elements

# By ID
element_by_id = driver.find_element(By.ID, 'element_id')

# By Name
element_by_name = driver.find_element(By.NAME, 'element_name')

# By Class Name
element_by_class = driver.find_element(By.CLASS_NAME, 'element_class')

# By Tag Name
element_by_tag = driver.find_element(By.TAG_NAME, 'input')

# By CSS Selector
element_by_css = driver.find_element(By.CSS_SELECTOR, 'div.classname > input#input_id')

# By XPath
element_by_xpath = driver.find_element(By.XPATH, '//input[@id="input_id"]')

# Finding Multiple Elements
elements_list = driver.find_elements(By.CLASS_NAME, 'elements_class')

# Interacting with Elements

# Clicking
button = driver.find_element(By.ID, 'submit_button')
button.click()

# Sending Keys
text_field = driver.find_element(By.NAME, 'username')
text_field.send_keys('my_username')

# Clearing Text
text_field.clear()

# Submitting a Form
form = driver.find_element(By.ID, 'login_form')
form.submit()

# Waiting for Elements

# Implicit Waits
driver.implicitly_wait(10)  # Wait up to 10 seconds for elements to be found

# Explicit Waits
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Create a WebDriverWait object
wait = WebDriverWait(driver, 10)

# Wait until the element is present
element = wait.until(EC.presence_of_element_located((By.ID, 'element_id')))

# Handling Alerts

# Wait for the alert to be present
alert = wait.until(EC.alert_is_present())

# Switch to the alert
alert = driver.switch_to.alert

# Accept the alert
alert.accept()

# Dismiss the alert
alert.dismiss()

# Get alert text
alert_text = alert.text

# Send keys to alert (if prompt)
alert.send_keys('Some text')

# Handling Frames and IFrames

# Switching to a Frame

# Switch by frame name or ID
driver.switch_to.frame('frame_name')

# Switch by index
driver.switch_to.frame(0)

# Switch by WebElement
frame_element = driver.find_element(By.TAG_NAME, 'iframe')
driver.switch_to.frame(frame_element)

# Switching Back to Default Content
driver.switch_to.default_content()

# Handling Windows and Tabs

# Getting Window Handles

# Get the current window handle
main_window = driver.current_window_handle

# Get all window handles
windows = driver.window_handles

# Switching to a Window
driver.switch_to.window(window_handle)

# Opening a New Tab
driver.execute_script("window.open('');")
# Switch to the new tab
driver.switch_to.window(driver.window_handles[-1])

# Closing a Tab or Window
driver.close()
# Switch back to the main window if needed
driver.switch_to.window(main_window)

# Taking Screenshots

# Full Page Screenshot
driver.save_screenshot('screenshot.png')

# Element Screenshot
element = driver.find_element(By.ID, 'element_id')
element.screenshot('element_screenshot.png')

# Executing JavaScript

# Scroll to the bottom of the page
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

# Return a value from JavaScript
title = driver.execute_script("return document.title;")

# Handling Cookies

# Getting Cookies

# Get all cookies
cookies = driver.get_cookies()

# Get a specific cookie
cookie = driver.get_cookie('cookie_name')

# Adding a Cookie
cookie = {'name': 'my_cookie', 'value': 'cookie_value'}
driver.add_cookie(cookie)

# Deleting Cookies

# Delete a specific cookie
driver.delete_cookie('cookie_name')

# Delete all cookies
driver.delete_all_cookies()

# Closing the Browser

# Close Current Window
driver.close()

# Quit the WebDriver Session
driver.quit()

# Additional Tips

# Maximizing and Minimizing Window

# Maximize window
driver.maximize_window()

# Minimize window
driver.minimize_window()

# Navigating Back and Forward

# Navigate back
driver.back()

# Navigate forward
driver.forward()

# Refreshing the Page
driver.refresh()

# Getting Page Source
page_source = driver.page_source

# Getting Current URL
current_url = driver.current_url

# Getting Page Title
title = driver.title

# Examples

# Example: Logging into a Website
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Initialize WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Navigate to login page
driver.get('https://www.example.com/login')

# Find username and password fields
username_field = driver.find_element(By.ID, 'username')
password_field = driver.find_element(By.ID, 'password')

# Enter credentials
username_field.send_keys('my_username')
password_field.send_keys('my_password')

# Click the login button
login_button = driver.find_element(By.ID, 'login_button')
login_button.click()

# Wait for the next page to load
driver.implicitly_wait(5)

# Verify login by checking for a specific element
if driver.find_elements(By.ID, 'logout_button'):
    print('Login successful!')
else:
    print('Login failed.')

# Close the browser
driver.quit()

# Example: Scraping Data from a Table
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Initialize WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://www.example.com/table')

# Find the table element
table = driver.find_element(By.TAG_NAME, 'table')

# Find all rows in the table
rows = table.find_elements(By.TAG_NAME, 'tr')

# Iterate over rows and extract data
for row in rows:
    cells = row.find_elements(By.TAG_NAME, 'td')
    data = [cell.text for cell in cells]
    print(data)

# Close the browser
driver.quit()

# Common Exceptions

# NoSuchElementException: Raised when an element is not found.
from selenium.common.exceptions import NoSuchElementException

try:
    element = driver.find_element(By.ID, 'non_existent_id')
except NoSuchElementException:
    print('Element not found.')

# TimeoutException: Raised when a command times out.
from selenium.common.exceptions import TimeoutException

try:
    element = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.ID, 'element_id'))
    )
except TimeoutException:
    print('Loading took too much time!')

# Best Practices

# Use Explicit Waits: Prefer explicit waits over implicit waits for better control.

# Exception Handling: Always handle exceptions to prevent your script from crashing.

# Resource Cleanup: Ensure that driver.quit() is called to close the browser and end the session.

# Avoid Hardcoded Waits: Instead of time.sleep(), use WebDriverWait to wait for specific conditions.

# Use CSS Selectors or XPath Wisely: Choose selectors that are less likely to change.

# Note: Remember to comply with the website's terms of service and robots.txt file when scraping data.
# Always practice ethical scraping.