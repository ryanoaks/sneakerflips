import requests
import json
import re

product_list = []

def search_products(url, headers):
    r = requests.get(url, headers=headers)
    parse_products(url, r.text)

def get_product_list():
    return product_list

def parse_products(url,text):
    jsn = json.loads(text)
    for product in jsn['products']:

        product_name = product['name']
        product_sku = product['sku']
        
        product_url = create_product_url(url, product_sku, product_name)
        product_sku = product_sku[:-3] + '-' + product_sku[-3:]
        #product_original_price = product['originalPrice']['value']
        product_sale_price = product['price']['value']
        brand = product['name'].split()[0]

        #format name to use with stockx search url
        print("Formatting Stockx Request URL")
        name = product_name.replace("- ", "")
        #name = name.replace(" ", "-")
        name = name.replace("'", "")
        name = name.replace('"', "")

        pattern = 'Boys|Girls|Womens|Mens'
        name = re.sub(pattern, "", name)

        formatted_name = name.replace(' ', '%20').lower()


        if brand == 'Nike':
        #sku = sku[:-3] + '-' + sku[-3:]
            search_param = formatted_name

        elif brand == 'adidas':
            search_param = product_sku

        else:
            search_param = None

        #format_url(brand, product_name, product_sku)
        product_list.append({'sku':product_sku, 'name':product_name, 'product_sale_price': product_sale_price, 'brand':brand, 'product_url': product_url, 'search_param': search_param})
        
def create_product_url(url, sku, name):
    site = url.split('.')[1]
    base = "https://www.{}.com/product/".format(site)
    sku = sku.replace("'", "")
    name = name.replace("- ", "")
    name = name.replace(" ", "-")
    name = name.replace("'", "")
    name = name.replace('"', "")
    s = name + '/' + sku + '.html'
    url = base + s

    return url