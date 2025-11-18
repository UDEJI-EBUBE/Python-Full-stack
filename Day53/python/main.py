import time

import requests
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

FORMS_URL = "____"
WEB_URL = "____"

response = requests.get(WEB_URL)
zillow = response.text

soup = BeautifulSoup(zillow, "html.parser")
prices = soup.find_all(name="span", class_="PropertyCardWrapper__StyledPriceLine")
prices_list = [price.get_text().replace("/mo", "").split("+")[0] for price in prices if "$" in price.text]

address = soup.find_all(name="address")
address_list = [addresses.get_text() for addresses in address]

link = soup.find_all(name="div", class_="StyledPropertyCardDataWrapper")
link_list = [links.get_text() for links in link]

print(prices_list)
print(address_list)
print(link_list)

driver = webdriver.Chrome()
for _ in range(len(link_list)):
    driver.get(FORMS_URL)
    time.sleep(5)

    address_form = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')))
    address_form.send_keys(address_list[_])

    price_form = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')))
    price_form.send_keys(prices_list[_])

    link_form = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')))
    link_form.send_keys(link_list[_])

    submit = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span')))
    submit.click()

    time.sleep(5)
