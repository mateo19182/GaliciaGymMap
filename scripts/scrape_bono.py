from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
import csv

# Setup Selenium Chrome WebDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Open the target webpage
driver.get("https://app.bonodeporte.gal/#/merchants/list?pagination=1342")

# Wait for the dynamic content to load
time.sleep(10)  # Increased time for dynamic content to fully load

# Extract all visible text from the body of the webpage
all_text = driver.find_element(By.TAG_NAME, "body").text

# Close the browser
driver.quit()

# Split the text by lines and filter out empty lines
lines = [line.strip() for line in all_text.split('\n') if line.strip()]

# Initialize an empty list to store the scraped data
data = [['Name', 'Address', 'Postal Code', 'Location']]

# Dynamically find the starting index for the list of establishments
# Assuming "Buscar establecementos" is a stable marker that precedes the data
try:
    start_index = lines.index("Buscar establecementos") + 2
except ValueError:
    start_index = None

if start_index:
    i = start_index
    while i < len(lines):
        # Skipping 'web' or 'map' lines
        if lines[i] == 'web' or lines[i] == 'map':
            i += 1
            continue  # Skip this iteration and move to the next line

        # Extract details for each establishment
        try:
            name = lines[i]
            address = lines[i + 1]
            postal_code = lines[i + 2]
            location = lines[i + 3]
            data.append([name, address, postal_code, location])
            i += 4  # Move to the next block of establishment data
        except IndexError:
            # Break the loop if there are not enough lines left for a full record
            break
        

    # Write data to a CSV file
    with open('establishments.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(data)

    print("Data scraped and saved to establishments.csv")
else:
    print("Failed to find the starting index for establishments.")
