# Web scraper to download electoral results from Panama's Electoral Tribunal
# Main URL: https://resultados.te.gob.pa/resultados/100

# Load libraries
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Set up and initialize the webdriver 
options = webdriver.ChromeOptions()
options.add_argument('--headless')
driver = webdriver.Chrome(service=Service(), options=options)

# Get the URL
base_url = "https://resultados.te.gob.pa/resultados/100/presidente/1"
driver.get(base_url + "/provincia/1/distrito/0")

# Extract table elements
table = driver.find_elements(By.CLASS_NAME, "tbody")
table_rows = table.find_elements(By.TAG_NAME, "tr")
print(table_rows)
for row in table_rows:
    print(row.text)