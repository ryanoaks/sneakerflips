import requests
import csv
import random

# import os
# import zipfile

# from selenium import webdriver


# PROXY_HOST = 'us-pr.oxylabs.io'  # rotating proxy or host
# PROXY_PORT = 10000 # port
# PROXY_USER = 'customer-yxrp8316-sessid-hw166417678' # username
# PROXY_PASS = 'H1Atrusoiqq8316' # password


# manifest_json = """
# {
#     "version": "1.0.0",
#     "manifest_version": 2,
#     "name": "Chrome Proxy",
#     "permissions": [
#         "proxy",
#         "tabs",
#         "unlimitedStorage",
#         "storage",
#         "<all_urls>",
#         "webRequest",
#         "webRequestBlocking"
#     ],
#     "background": {
#         "scripts": ["background.js"]
#     },
#     "minimum_chrome_version":"22.0.0"
# }
# """

# background_js = """
# var config = {
#         mode: "fixed_servers",
#         rules: {
#         singleProxy: {
#             scheme: "http",
#             host: "%s",
#             port: parseInt(%s)
#         },
#         bypassList: ["localhost"]
#         }
#     };

# chrome.proxy.settings.set({value: config, scope: "regular"}, function() {});

# function callbackFn(details) {
#     return {
#         authCredentials: {
#             username: "%s",
#             password: "%s"
#         }
#     };
# }

# chrome.webRequest.onAuthRequired.addListener(
#             callbackFn,
#             {urls: ["<all_urls>"]},
#             ['blocking']
# );
# """ % (PROXY_HOST, PROXY_PORT, PROXY_USER, PROXY_PASS)


# def get_chromedriver(use_proxy=False, user_agent=None):
#     path = os.path.dirname(os.path.abspath(__file__))
#     chrome_options = webdriver.ChromeOptions()
#     chrome_options.headless = False
#     if use_proxy:
#         pluginfile = 'proxy_auth_plugin.zip'

#         with zipfile.ZipFile(pluginfile, 'w') as zp:
#             zp.writestr("manifest.json", manifest_json)
#             zp.writestr("background.js", background_js)
#         chrome_options.add_extension(pluginfile)
#     if user_agent:
#         chrome_options.add_argument('--user-agent=%s' % user_agent)
#     driver = webdriver.Chrome(
#         os.path.join(path, 'chromedriver'),
#         options=chrome_options)
#     return driver

# def main(request_url):
#     driver = get_chromedriver(use_proxy=True)
#     #driver.get('https://www.google.com/search?q=my+ip+address')
#     response = driver.get(request_url).json()
#     print(response)
#     return response

# proxy_list = []



# create_proxylist()

# proxylist = []

# import sys
# import urllib.request, socket
# from threading import Thread

# socket.setdefaulttimeout(30)

# def check_proxy(proxy):
#     print(proxy)
#     try:        
#         proxy_handler = urllib.request.ProxyHandler({'https': proxy, 'http': proxy})     
#         opener = urllib.request.build_opener(proxy_handler)
#         opener.addheaders = [('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36')]
#         #urllib.request.install_opener(opener) 
#         sock = urllib.request.urlopen('https://httpbin.org/ip', timeout=5)
#         print(sock.http)       

#         proxylist.append(sock)
#         print(proxy)
#     except urllib.error.HTTPError as e:        
#         return e
#     except Exception as detail:
#         return detail
#     return 0

# #Example run : echo -ne "192.168.1.1:231\n192.168.1.2:231" | python proxy_checkpy3-async.py
# threads = []
    
proxylist = []

def create_proxylist():
    with open('/Users/ryanoaks/Documents/Dev/Sneakers/Sites v2/ip_proxies.csv','r') as f:
        reader = csv.reader(f)
        for proxy in reader:
            proxylist.append(proxy[0])

#         for proxy in reader:
#             thread = Thread(target=check_proxy, args=(proxy,))
#             thread.start()
#             threads.append(thread)

#         for thread in threads:
#             thread.join()

    print(proxylist)

def get_proxy():
    return random.choice(proxylist)

create_proxylist()
print(get_proxy())
