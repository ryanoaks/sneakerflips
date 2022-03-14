import requests
import json
from webhook import *
from stockx_alt import *
from match import *


#initial request to get number of pages
page_request = requests.get('https://api.nike.com/cic/browse/v1?queryid=products&anonymousId=FB1FAE69C54E5225BAFCDC4F531EEC30&country=us&endpoint=%2Fproduct_feed%2Frollup_threads%2Fv2%3Ffilter%3Dmarketplace(US)%26filter%3Dlanguage(en)%26filter%3DemployeePrice(true)%26filter%3DattributeIds(16633190-45e5-4830-a068-232ac7aea82c%2C5b21a62a-0503-400c-8336-3ccfbff2a684)%26anchor%3D0%26consumerChannelId%3Dd9a5bc42-4b9c-4976-858a-f159cf99c647%26count%3D24&language=en&localizedRangeStr=%7BlowestPrice%7D%20%E2%80%94%20%7BhighestPrice%7D')
pages = json.loads(page_request.text)
#print(page_request.text)
n_pages = pages['data']['products']['pages']['totalPages']

def request():
    for page in range(0,n_pages,1): 
        p = (page * 24)
        #url = 'https://api.nike.com/cic/browse/v1?queryid=products&anonymousId=FB1FAE69C54E5225BAFCDC4F531EEC30&country=us&endpoint=%2Fproduct_feed%2Frollup_threads%2Fv2%3Ffilter%3Dmarketplace(US)%26filter%3Dlanguage(en)%26filter%3DemployeePrice(true)%26filter%3DattributeIds(16633190-45e5-4830-a068-232ac7aea82c%2C5b21a62a-0503-400c-8336-3ccfbff2a684)%26anchor%3D{}%26consumerChannelId%3Dd9a5bc42-4b9c-4976-858a-f159cf99c647%26count%3D24&language=en&localizedRangeStr=%7BlowestPrice%7D%20%E2%80%94%20%7BhighestPrice%7D'.format(p)
        #url = 'https://api.nike.com/cic/browse/v1?queryid=products&anonymousId=FB1FAE69C54E5225BAFCDC4F531EEC30&country=us&endpoint=%2Fproduct_feed%2Frollup_threads%2Fv2%3Ffilter%3Dmarketplace(US)%26filter%3Dlanguage(en)%26filter%3DemployeePrice(true)%26filter%3DattributeIds(0f64ecc7-d624-4e91-b171-b83a03dd8550%2C16633190-45e5-4830-a068-232ac7aea82c)%26anchor%3D{}%26consumerChannelId%3Dd9a5bc42-4b9c-4976-858a-f159cf99c647%26count%3D24&language=en&localizedRangeStr=%7BlowestPrice%7D%20%E2%80%94%20%7BhighestPrice%7D'.format(p)
        url = 'https://api.nike.com/cic/browse/v1?queryid=products&anonymousId=FB1FAE69C54E5225BAFCDC4F531EEC30&country=us&endpoint=%2Fproduct_feed%2Frollup_threads%2Fv2%3Ffilter%3Dmarketplace(US)%26filter%3Dlanguage(en)%26filter%3DemployeePrice(true)%26filter%3DattributeIds(16633190-45e5-4830-a068-232ac7aea82c%2C498ac76f-4c2c-4b55-bbdc-dd37011887b1)%26anchor%3D{}%26consumerChannelId%3Dd9a5bc42-4b9c-4976-858a-f159cf99c647%26count%3D24&language=en&localizedRangeStr=%7BlowestPrice%7D%20%E2%80%94%20%7BhighestPrice%7D'.format(p)
        r = requests.get(url)
        data = json.loads(r.text)
        print("PAGE # {}".format(page))
        parse_data(data)


def parse_data(data):
    try:
        for d in data['data']['products']['products']:
            #print(d)
            for c in d['colorways']:
                name = c['pdpUrl'].split('/')[2].rsplit('-',1)[0].replace('-', ' ')
                sku = c['pdpUrl'].split('/')[3]
                price = c['price']['currentPrice']
                url = 'https://www.nike.com{}'.format(c['pdpUrl'].replace('{countryLang}',''))
                image = c['images']['squarishURL']
                #print("SKU: {} PRICE: {} URL: {}".format(name, price, url))
                brand = 'Nike'

                product = {
                    'sku':sku,
                    'brand':brand, 
                    'product_sale_price':price, 
                    'product_url':url
                    }

                try:
                    request_url = stockx_format_request(sku)
                    raw_request_data = browser_request(request_url)
                    stockx_parse_json(raw_request_data, product)
                    #match(stockx_shoe, product)
                except:
                    pass
    except:
        pass

request()