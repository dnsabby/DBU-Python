#Web Scraping with Selenium in Python
#To use: run pip install selenium webdriver-manager

# Import necessary modules for browser automation and data handling
from selenium import webdriver  # Selenium WebDriver for browser automation
from selenium.webdriver.chrome.service import Service  # Service class to manage the ChromeDriver executable
from selenium.webdriver.common.by import By  # Module for specifying element locating strategies
from selenium.webdriver.support.ui import WebDriverWait  # For implementing explicit waits
from selenium.webdriver.support import expected_conditions as EC  # Expected conditions to use with waits
from webdriver_manager.chrome import ChromeDriverManager  # Automatically handles ChromeDriver installation
import json  # Module for working with JSON data

# Initialize the Chrome WebDriver using the Service class and ChromeDriverManager
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Navigate to the target website for scraping
driver.get('http://books.toscrape.com/')

# Initialize an empty list to store the scraped book data
books_data = []

# Create a WebDriverWait object with a maximum timeout of 10 seconds
wait = WebDriverWait(driver, 10)

# Wait until all elements with the class name 'FIND_THE_CLASS_ELEMENT' are present in the DOM
wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'FIND_THE_CLASS_ELEMENT')))

# Locate all elements on the page with the class name 'FIND_THE_CLASS_ELEMENT'
books = driver.find_elements(By.CLASS_NAME, 'FIND_THE_CLASS_ELEMENT')

# Loop through the first 10 book elements to extract data
for book in books[:10]:  # Limit to top 10 books
    # Extract the title of the book from the 'title' attribute of the 'FIND_THE_TAG_ELEMENT' tag within 'FIND_THE_TAG_ELEMENT'
    title = book.find_element(By.TAG_NAME, 'FIND_THE_TAG_ELEMENT').find_element(By.TAG_NAME, 'FIND_THE_TAG_ELEMENT').get_attribute('title')
    # Extract the price of the book from the element with class 'FIND_THE_CLASS_ELEMENT'
    price = book.find_element(By.CLASS_NAME, 'FIND_THE_CLASS_ELEMENT').text
    # Append the extracted data as a dictionary to the books_data list
    books_data.append({'title': title, 'price': price})

# Open a JSON file in write mode with UTF-8 encoding to save the scraped data
with open('books_top10.json', 'w', encoding='utf-8') as f:
    # Write the books_data list to the JSON file with indentation for readability
    json.dump(books_data, f, indent=4, ensure_ascii=False)

# Print the list of scraped books and their prices to the console for verification
print(books_data)

# Close the browser and terminate the WebDriver session to free up resources
driver.quit()