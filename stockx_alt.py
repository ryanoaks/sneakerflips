import json
import requests
import re


import concurrent.futures

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys

from match import *
from proxies import *

stockx_list = []

print("****OPENING BROWSER****")
#options = Options()
#options.headless = True
#browser = webdriver.Firefox(options=options)


headers = "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"

def browser_request(request_url):
    if request_url is None:
        pass
    else:
        try:
            print("getting proxy")
            proxy = get_proxy()
            # print("proxy: {}".format(proxy))
            headers = {'User-Agent':"Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"}
            print("Making request")
            r = requests.get(request_url, headers=headers, proxies={'https':proxy, 'http':proxy}, timeout=10)
            print(r.json())
            return r.json()
        except:
            pass
        # finally:
        #     browser_request.close()

def stockx_parse_json(stockx_json, other_shoe):
 
    d = stockx_json
    print("PARSING JSON")
    for product in d['Products']:
        stockx_sku = product['traits'][0]['value']
        image_url = product['media']['thumbUrl']
        name = product['title']
        print(name)
        sales_this_period = product['market']['salesThisPeriod']
        sales_last_72_hours = product['market']['salesLast72Hours']
        stockx_lowest_ask = product['market']['lowestAsk']
        urlkey = product['urlKey']
        url = 'https://www.stockx.com/{}'.format(urlkey)

        stockx_shoe = {
            'stockx_sku': stockx_sku, 
            'lowest_ask': stockx_lowest_ask, 
            'image_url': image_url, 
            'stockx_name': name, 
            'sales_this_period': sales_this_period, 
            'sales_last_72_hours': sales_last_72_hours, 
            'stockx_url': url 
            }

        match(other_shoe, stockx_shoe)

def get_stockx_list():
    return stockx_list

def stockx_format_request(search_param):
    request_url = "https://stockx.com/api/browse?&_search=" + search_param + "&dataType=product"
    return request_url


