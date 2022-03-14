import re
from webhook import send_webhook

match_list = []
profit_found_list = []

def match(first_shoe, stockx_shoe):
    
    #searched shoe data
    sku = first_shoe['sku']
    brand = first_shoe['brand']
    price = first_shoe['product_sale_price']
    product_url = first_shoe['product_url']

    #stockx shoe data   
    stockx_sku = stockx_shoe['stockx_sku']
    stockx_lowest_ask = stockx_shoe['lowest_ask']
    image_url = stockx_shoe['image_url']
    product_name = stockx_shoe['stockx_name']
    sales_this_period = stockx_shoe['sales_this_period']
    sales_last_72_hours = stockx_shoe['sales_last_72_hours']
    stockx_url = stockx_shoe['stockx_url']



    print("Nike: {}, StockX: {}".format(sku, stockx_sku))
    if brand == 'Nike':
        try:
            if re.search(sku, stockx_sku):
                find_profit(first_shoe, stockx_shoe)
                print("match: {}".format(sku))
            elif re.search('\w+' + sku, stockx_sku):
                find_profit(first_shoe, stockx_shoe)
            elif re.search('\w+' + sku, stockx_sku.split('/')[0]):
                find_profit(first_shoe, stockx_shoe)
            elif re.search('\w+' + sku, stockx_sku.split('/')[1]):
                find_profit(first_shoe, stockx_shoe)
            else:
                print("Not Match")
                pass
                
        except:
            pass

    elif brand == 'adidas':
        if re.search(sku, stockx_sku):
            find_profit(first_shoe, stockx_shoe)
        else:
            pass

def get_match_list():
    return match_list


def find_profit(shoe, stockx):
    shoe.update(stockx)
    print(shoe)
    discount = .2
    stockx_payout = shoe['lowest_ask'] * .89
    
    if discount:
        discount_amount = shoe['product_sale_price'] * discount
        buy_price = (shoe['product_sale_price'] - discount_amount) * 1.0725
        shoe['product_sale_price'] = buy_price
    else:
        buy_price = shoe['product_sale_price'] * 1.0725
    if buy_price < stockx_payout and shoe['sales_this_period'] > 3:
        profit = stockx_payout - buy_price
        shoe['profit'] = profit
        send_webhook(shoe)
        #profit_found_list.append(item)

    #return profit_found_list