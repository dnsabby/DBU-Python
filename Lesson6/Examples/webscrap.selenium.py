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
driver.get('http://quotes.toscrape.com/')

# Initialize an empty list to store the scraped quotes and authors
quotes_data = []

# Create a WebDriverWait object with a maximum timeout of 10 seconds
wait = WebDriverWait(driver, 10)

# Wait until all elements with the class name 'quote' are present in the DOM
wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'quote')))

# Locate all elements on the page with the class name 'quote'
quotes = driver.find_elements(By.CLASS_NAME, 'quote')

# Loop through the first 10 quote elements to extract data
for quote in quotes[:10]:  # Limit to top 10 quotes
    # Extract the quote text from the child element with class 'text'
    text = quote.find_element(By.CLASS_NAME, 'text').text
    # Extract the author's name from the child element with class 'author'
    author = quote.find_element(By.CLASS_NAME, 'author').text
    # Append the extracted data as a dictionary to the quotes_data list
    quotes_data.append({'quote': text, 'author': author})

# Open a JSON file in write mode with UTF-8 encoding to save the scraped data
with open('quotes_top10.json', 'w', encoding='utf-8') as f:
    # Write the quotes_data list to the JSON file with indentation for readability
    json.dump(quotes_data, f, indent=4, ensure_ascii=False)

# Print the list of scraped quotes and authors to the console for verification
print(quotes_data)

# Close the browser and terminate the WebDriver session to free up resources
driver.quit()