from bs4 import BeautifulSoup
import time 
import pandas as pd
from selenium import webdriver
import csv
start_url="https://exoplanets.nasa.gov/discovery/exoplanet-catalog/"
browser=webdriver.Chrome("chromedriver")
browser.get(start_url)
time.sleep(10)

def scrape():
    headers=["name","light_years_from_earth","planet_mass","stellar_magnitude","discovery_date"]
    planet_data=[]
    for i in range(0, 201):
        soup=BeautifulSoup(browser.page_source,"html.parser")
        for utag in soup.find_all("ul",attrs={"class","exoplanet"}):
            li_tags=utag.find_all("li")
            temp_list=[]
            for index,li_tag in enumerate(li_tags):
                if index == 0:
                    temp_list.append(li_tag.find_all("a")[0].contents[0])
            else:
                try:
                    temp_list.append(li_tag.contents[0])
                except:
                    temp_list.append("")
            planet_data.append(temp_list)
    with open("scraper.csv","w") as f:
        csvwriter=csv.writer(f)
        csvwriter.writerow(headers)
        csvwriter.writerows(planet_data)

scrape()


