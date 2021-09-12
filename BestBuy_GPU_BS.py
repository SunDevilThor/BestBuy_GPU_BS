# Best Buy GPU Scraper using Beautiful Soup

import requests
from bs4 import BeautifulSoup
from requests.api import head
import pandas as pd

def extract():
    url = 'https://www.bestbuy.com/site/searchpage.jsp?st=rtx+3080&_dyncharset=UTF-8&_dynSessConf=&id=pcat17071&type=page&sc=Global&cp=1&nrp=&sp=&qp=&list=n&af=true&iht=y&usc=All+Categories&ks=960&keys=keys'
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    #print(response.status_code)
    return soup

        
def transform(soup):
    products = soup.find_all('li', class_='sku-item')
    #print(len(products))
    for item in products:
        title = item.find('h4', class_ = 'sku-header').text
        #print(title)
        price = item.find('div', class_= 'priceView-hero-price')
        for dollars in price:
            dollars = item.find('span', class_='sr-only').text
            #print(dollars)
            words = dollars.split(' ')
            currency = (words[-1])
            #print(currency)
        status = item.find('div', class_='sku-list-item-button').text
        # print(status)
        link = item.find('a', href=True)
        product_url = 'http://www.bestbuy.com/' + link['href']
        print(product_url)

        gpu = {
            'title': title,
            'price': currency,
            'status': status,
            'link': product_url, 
        }

        GPUs.append(gpu)

    return 

GPUs = []

c = extract()
transform(c)

df = pd.DataFrame(GPUs)
print(df)
df.to_csv('BestBuy_GPU_BS.csv')
df.to_json('BestBuy_GPU_BS.json')

# NOTES:
# sku = item.find('span', class_= 'sku-value'[1])   ----- Returns first item, which is model
