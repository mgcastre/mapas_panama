# Source: Hoyalytics Analyst Training, data science track

#Necessary imports
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

import datetime
import pandas as pd

start_date = datetime.date(2023, 1, 1)
end_date = datetime.date(2023, 1, 31)
current_date = start_date

time_delta = datetime.timedelta(days=1)


# Set up the webdriver (optional argument to run headless)
options = webdriver.ChromeOptions()
#options.add_argument('--headless')

#initialize the webdriver to use the chrome browser
driver = webdriver.Chrome(service=Service(), options=options)

locations = pd.DataFrame(columns = ["Date", "Location", "Open", "Close"])

while current_date <= end_date:
    url = "https://www.hoyaeats.com/menu-hours/?date={}".format(current_date.strftime("%Y-%m-%d"))

    #use selenium to load the webpage
    driver.get(url)


    #get a list of all the trs with classnames of location and row
    table_rows = driver.find_elements(By.CLASS_NAME, "location.row")

    print("Number of locations: " + str(len(table_rows)))

    for table_row in table_rows:
        #get the name of the location
        location_name = table_row.find_element(By.TAG_NAME, "a").get_attribute("innerText")

        hour_rows = table_row.find_elements(By.CLASS_NAME, "hours.hours-row")
        for hour_row in hour_rows:
            open_at_text = hour_row.find_element(By.CLASS_NAME, "open_at").get_attribute("innerText")
            close_at_text = hour_row.find_element(By.CLASS_NAME, "close_at").get_attribute("innerText")
            locations = locations._append({"Date": current_date.strftime("%Y-%m-%d"), "Location": location_name, "Open": open_at_text, "Close": close_at_text}, ignore_index=True)
        print("Currently scraping: " + current_date.strftime("%Y-%m-%d") + location_name)

    current_date += time_delta
#quit
locations.to_csv("hoya_eats.csv")
input("Press Enter to quit the program...")

driver.quit()
