import requests
import json
import time
import emailsend
import db
from datetime import datetime, date


def jprint(obj):
    text = json.dumps(obj, sort_keys= True, indent=4)
    return text
try:
    db.createtable()
except:
    pass
try:
    idc = db.getlastid("DogeCoin")+1
    idi = idc
except:
    idc = 1
    idi = idc
max_doge = 0
min_doge = 0

max_btc = 0
min_btc = 0

max_eth = 0
min_eth = 0

for i in range(15):
    time.sleep(5)
    response = requests.get("https://api.wazirx.com/api/v2/tickers")
    # doge
    doge = jprint(response.json()['dogeinr'])
    price_doge = float(doge.split(",")[2].split(":")[1][2:-1])
    open_price_doge = float(doge.split(",")[7].split(":")[1])
    max_doge_price = float(doge.split(',')[3].split(":")[1][2:-1])
    min_doge_price = float(doge.split(',')[5].split(":")[1][2:-1])

    diff_doge = price_doge - open_price_doge
    gain_loss_doge = float("{:.2f}".format((diff_doge/price_doge)*100))

    #btc
    btc = jprint(response.json()['btcinr'])
    price_btc = float(btc.split(",")[2].split(":")[1][2:-1])
    open_price_btc = float(btc.split(",")[7].split(":")[1])
    max_btc_price = float(btc.split(',')[3].split(":")[1][2:-1])
    min_btc_price = float(btc.split(',')[5].split(":")[1][2:-1])

    diff_btc = price_btc - open_price_btc
    gain_loss_btc =  float("{:.2f}".format((diff_btc/price_btc)*100))
    
    #eth
    eth = jprint(response.json()['ethinr'])
    price_eth = float(eth.split(",")[2].split(":")[1][2:-1])
    open_price_eth = float(eth.split(",")[7].split(":")[1])
    max_eth_price = float(eth.split(',')[3].split(":")[1][2:-1])
    min_eth_price = float(eth.split(',')[5].split(":")[1][2:-1])

    diff_eth = price_eth - open_price_eth
    gain_loss_eth =  float("{:.2f}".format((diff_btc/price_btc)*100))


    tim = datetime.now()
    dat = date.today()
    curr_date = dat.strftime("%d-%m-%Y")

    curr_time = tim.strftime("%H:%M:%S")

    max_doge = max(max_doge, max_doge_price)
    if(idc== idi):
        min_doge = min_doge_price
    else:
        min_doge = min(min_doge, min_doge_price)

    max_btc = max(max_btc, max_btc_price)
    if(idc== idi):
        min_btc = min_btc_price
    else:
        min_btc = min(min_btc, min_btc_price)

    max_eth = max(max_eth, max_eth_price)
    if(idc== idi):
        min_eth = min_eth_price
    else:
        min_eth = min(min_eth, min_eth_price)

    # inserting in doge
    db.inserttable("DogeCoin",idc, "DOGE", (price_doge), (gain_loss_doge),(max_doge), (min_doge), str(curr_time), curr_date)

    # inserting in btc 
    db.inserttable("BitCoin", idc, "BTC", (price_btc), (gain_loss_btc),(max_btc), (min_btc), str(curr_time), curr_date)

    # inserting in eth 
    db.inserttable("Ethereum", idc, "ETH", (price_eth), (gain_loss_eth),(max_eth), (min_eth), str(curr_time), curr_date)

    idc+=1
    print("Success!")

    

    if(gain_loss_doge>=50):
        msg = "Current price of DOGE is {} and the gain/loss is {}".format(price_doge, gain_loss_doge)
        emailsend.sende(msg)
        break

print(max_doge)
print(min_doge)

# test cod
# response = requests.get("https://api.wazirx.com/api/v2/market-status")
# count = 0
# for i in range(100):
#     a = jprint(response2.json())
# for i in range(10):
#     a = jprint(response.json()['assets'][i])
#     print(a)
# for i in range(314):
#     a = jprint(response.json()['markets'][i])
    # b = "usdt"
    # if(a==b):
    #     count = i
    # print(a)
# print(count)

# a = jprint(response.json()['markets'][285])
# price = a[85:100].split('"')[0]
# print(price)
# print(count)
# a = jprint(response.json()['markets'][194])

# print(a[81:96].split('"')[1])
# doge = jprint(response.json()['markets'][285])
# wrx = jprint(response.json()['markets'][194])
# usdt = jprint(response.json()['markets'][296])

# price_doge = float(doge.split(',')[3].split(':')[1][2:-1])
# price_wrx = float(wrx.split(',')[3].split(':')[1][2:-1])

# doge_price_inr = price_doge*price_wrx*77.49
# print(doge_price_inr)