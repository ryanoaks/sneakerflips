#from discord_webhook import DiscordWebhook, DiscordEmbed
import discord
from discord import Webhook, RequestsWebhookAdapter

def send_webhook(data):
    print("SENDING WEBHOOK")
    stockx_sku = str(data['stockx_sku'])
    stockx_lowest_ask = str(data['lowest_ask'])
    image_url = str(data['image_url'])
    stockx_name = str(data['stockx_name'])
    sales_this_period = str(data['sales_this_period'])
    sales_last_72_hours = str(data['sales_last_72_hours'])
    stockx_url = str(data['stockx_url'])
    other_site_sku = str(data['sku'])
    other_site_price = str(data['product_sale_price'])
    other_site_url = str(data['product_url'])
    profit = str(data['profit'])

    print(stockx_name)

    webhook = Webhook.partial('714491448464113764','ZtrSo_wwoZoEMlgayGaUi9_f_OSanWSMgKDQfD7gAx8KtMh3gCF0EBShyrS0eNDzx8KW',adapter=RequestsWebhookAdapter())

    if int(sales_this_period) >= 15:
        color = discord.Color.green()
    elif 5 < int(sales_this_period) < 15:
        color = discord.Color.orange()
    else:
        color = discord.Color.red()

    embed = discord.Embed(
        title = stockx_name,
        description = stockx_sku,
        color = color
    )
    embed.set_thumbnail(url=image_url)
    embed.add_field(name="profit:", value="$" + profit)
    embed.add_field(name="LINKS:", value="[StockX]({}) | [Buy]({})".format(stockx_url, other_site_url))
    embed.add_field(name="Stockx Lowest Ask", value=stockx_lowest_ask)
    embed.add_field(name="72hr Sales", value=sales_last_72_hours, inline=True)
    embed.add_field(name="Sales This Period", value=sales_this_period, inline=True)
    
    webhook.send(embed=embed)


    










    #webhook = DiscordWebhook(url='https://discord.com/api/webhooks/790664120495374336/3xtMaRk1aIEvSPnZqwHULXDkJv7BGqouC7SrS0uFtGyXW2i1FQGbko-Ft2Mom4LT3n80')

    #embed = DiscordEmbed(
    # title="Embed Title", description="Your Embed Description", color=242424)
    
    # embed.set_author(
    #     name="name",
    #     url="www.facebook.com",
    #     icon_url="https://avatars0.githubusercontent.com/u/14542790",
    # )

    # embed.set_footer(text="Embed Footer Text")
    # embed.set_timestamp()

    # # Set `inline=False` for the embed field to occupy the whole line
    # #embed.add_embed_field(name='StockX URL', value=stockx_url)
    # #embed.add_embed_field(name='Buy URL', value=other_site_url)
    # #embed.add_embed_field(name='Buy Price', value="VALUE")
    # #embed.add_embed_field(name='Sales This Period', value=sales_this_period)
    # #embed.add_embed_field(name='Sales Last 72 Hours', value=sales_last_72_hours)
    # #embed.add_embed_field(name='Lowest Ask', value=stockx_lowest_ask)
    # embed.add_embed_field(name="Field 1", value="Lorem ipsum", inline=False)
    # embed.add_embed_field(name="Field 2", value="dolor sit", inline=False)
    # embed.add_embed_field(name="Field 3", value="amet consetetur")
    # embed.add_embed_field(name="Field 4", value="sadipscing elitr")
    # webhook.add_embed(embed)
    # response = webhook.execute()




# def discord(data):
#     stockx_sku = str(data['stockx_sku'])
#     stockx_lowest_ask = str(data['stockx_lowest_ask'])
#     image_url = str(data['image_url'])
#     stockx_name = str(data['product_name'])
#     sales_this_period = str(data['sales_this_period'])
#     sales_last_72_hours = str(data['sales_last_72_hours'])
#     stockx_url = str(data['stockx_url'])
#     other_site_sku = str(data['other_site_sku'])
#     other_site_price = str(data['other_site_price'])
#     other_site_url = str(data['other_site_url'])
#     profit = str(data['profit'])

#     webhook = DiscordWebhook(url='https://discord.com/api/webhooks/790664120495374336/3xtMaRk1aIEvSPnZqwHULXDkJv7BGqouC7SrS0uFtGyXW2i1FQGbko-Ft2Mom4LT3n80')

#     # create embed object for webhook
#     embed = DiscordEmbed(title=stockx_name, description=profit, color=242424)

#     # set author
#     embed.set_author(name=stockx_sku, url=stockx_url, icon_url=image_url)

#     # set image
#     #embed.set_image(url=image_url)

#     # set thumbnail
#     embed.set_thumbnail(url=image_url)

#     # set footer
#     #embed.set_footer(text='Embed Footer Text')

#     # set timestamp (default is now)
#     #embed.set_timestamp()

#     # add fields to embed
#     embed.add_embed_field(name='StockX URL', value=stockx_url)
#     embed.add_embed_field(name='Buy URL', value=other_site_url)
#     embed.add_embed_field(name='Buy Price', value=other_site_price)
#     embed.add_embed_field(name='Sales This Period', value=sales_this_period)
#     embed.add_embed_field(name='Sales Last 72 Hours', value=sales_last_72_hours)
#     embed.add_embed_field(name='Lowest Ask', value=stockx_lowest_ask)
#     # add embed object to webhook
#     webhook.add_embed(embed)

#     response = webhook.execute()
    
#     print(response)