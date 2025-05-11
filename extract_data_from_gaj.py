# 1.    Import Libraries
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pandas as pd


def extract_data_gaj(web_address, name_class, price_class):
    # 2.    Open chrome and website
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options= chrome_options)
    driver.get(web_address)


    # Find Elements
    name_element = driver.find_elements(By.CLASS_NAME, name_class)
    book_name = [b.text for b in name_element]

    price_element = driver.find_elements(By.CLASS_NAME, price_class)
    book_price = [p.text for p in price_element]

    df = pd.DataFrame({"Name": book_name, "Price": book_price})

    driver.quit()

    return df

gaj_address = "https://www.gajmarket.com/%D8%AE%D8%B1%DB%8C%D8%AF-%DA%A9%D8%AA%D8%A7%D8%A8-%D8%B9%D9%85%D9%88%D9%85%DB%8C"
gaj_name_class = "product-card__name"
gaj_price_class = "product-card__price"

gaj_df = extract_data_gaj(gaj_address, gaj_name_class, gaj_price_class)
gaj_df.to_csv("gaj_data.csv", index= False, encoding="utf-8")
print("Data saved!")

