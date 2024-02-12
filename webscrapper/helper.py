
from selenium.webdriver.common.keys import Keys

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import pandas as pd 
import requests

from bs4 import BeautifulSoup
import pandas as pd
import re


headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"
}

def build_url(item):
    url = f'https://www.canadacomputers.com/search/results_details.php?keywords={item}'
    return url

def get_data(url):
    response = requests.get(url, headers=headers).text
    soup = BeautifulSoup(response, "html.parser")
    all_titles = soup.findAll("span", attrs={"class": "productTemplate_title"})
    all_prices = soup.findAll("span", attrs={"class": "pq-hdr-product_price"})

    list_titles = []
    list_prices = []

    for title in all_titles:
        list_titles.append(title.string)

    #if do price.text instead of price.string it will print out more than just price
    for price in all_prices:
        list_prices.append(price.string)

    df = pd.DataFrame({'Title': list_titles, 'Price': list_prices})
    return df

def sort_df(df):
    df = df.sort_values(by='Price')
    df = df.reset_index(drop=True, inplace=False)

    return df
