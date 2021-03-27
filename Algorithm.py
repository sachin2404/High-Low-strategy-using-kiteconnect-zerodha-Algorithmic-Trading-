from kiteconnect import KiteConnect
from kiteconnect import KiteTicker
import logging
from High_Low_data import *


logging.basicConfig(level=logging.DEBUG)
api_key = ""
api_secret = ""
kite = KiteConnect(api_key, api_secret)
logging.basicConfig(level=logging.DEBUG)
#from below URL get request token
#https://kite.zerodha.com/connect/login?v=3&api_key=xxx
request_token = ""
#to obtain access token
#data = kite.generate_session(request_token,api_secret=api_secret)
#kite.set_access_token(data["access_token"])
access_token = ""
kite.set_access_token(access_token)
kws = KiteTicker(api_key, access_token)

niftystocks = ["ADANIPORTS", "ASIANPAINT", "AXISBANK", "BAJAJ-AUTO", "BAJAJFINSV", "BAJFINANCE", "BHARTIARTL", "BPCL",
               "BRITANNIA", "CIPLA", "COALINDIA", "DRREDDY", "EICHERMOT", "GAIL", "GRASIM", "HCLTECH", "HDFC",
               "HDFCBANK", "HEROMOTOCO", "HINDALCO", "HINDUNILVR", "IBULHSGFIN", "ICICIBANK", "INDUSINDBK",
               "INFY", "IOC", "ITC", "JSWSTEEL", "KOTAKBANK", "LT", "M&M", "MARUTI", "NTPC", "ONGC", "POWERGRID",
               "RELIANCE", "SBIN", "SUNPHARMA", "TATAMOTORS", "TATASTEEL", "TCS", "TECHM", "TITAN", "ULTRACEMCO", "UPL",
               "VEDL", "WIPRO", "YESBANK", "ZEEL"]
niftystocktokens = [3861249, 60417, 1510401, 4267265, 4268801, 81153, 2714625, 134657, 140033, 177665, 5215745, 225537,
                    232961, 1207553, 315393, 1850625, 340481, 341249, 345089, 348929, 356865, 7712001, 1270529, 1346049,
                    408065, 415745, 424961, 3001089, 492033, 2939649, 519937, 2815745, 2977281, 633601,
                    3834113, 738561, 779521, 857857, 884737, 895745, 2953217, 3465729, 897537, 2952193, 2889473, 784129,
                    969473, 3050241, 975873]


tendays_high=[]
fivedays_high=[]
tendays_low=[]
fivedays_low=[]
for i in range(49):
    tendays_high.append(tendayshigh(niftystocks[i]))
    fivedays_high.append(fivedayshigh(niftystocks[i]))
    tendays_low.append(tendayslow(niftystocks[i]))
    fivedays_low.append(fivedayslow(niftystocks[i]))
trade_done = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
              0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
              0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
stock_tick = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
              0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
              0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


def on_ticks(ws, ticks):
    # logging.debug("Ticks: {}".format(ticks))
    for i in range(49):
        for j in range(49):
            if (ticks[j]["instrument_token"] == niftystocktokens[i]):
                stock_tick[i] = ticks[j]["last_price"]
        print(stock_tick[i])
        print(niftystocks[i])
    def place_order(order_type,stock_price,stock_name):
        order_id = kite.place_order(variety="regular",
                                    exchange="NSE",
                                    tradingsymbol=stock_name,
                                    transaction_type=order_type,
                                    quantity=1,
                                    product="MIS",
                                    order_type="LIMIT",
                                    price=stock_price,
                                    validity="IOC",
                                    disclosed_quantity="None",
                                    trigger_price="None",
                                    tag="None")
        return order_id
    for i in range(50):
        if (stock_tick[i] >= tendays_high[i] and trade_done[i] == 0):
            order_id = place_order("BUY",stock_tick[i],niftystocks[i])
            trade_done[i] = 1
        elif (stock_tick[i] >= fivedays_high[i] and trade_done[i] == 0):
            order_id = place_order("BUY",stock_tick[i],niftystocks[i])
            trade_done[i] = 1
        elif (stock_tick[i] <= tendays_low[i] and trade_done[i] == 0):
            order_id = place_order("SELL",stock_tick[i],niftystocks[i])
            trade_done[i] = 1
        elif (stock_tick[i] <= fivedays_low[i] and trade_done[i] == 0):
            order_id = place_order("SELL",stock_tick[i],niftystocks[i])
            trade_done[i] = 1

def on_connect(ws, response):
    # Callback on successful connect.
    ws.subscribe(niftystocktokens)
    # Set LTP to tick in `full` mode.
    ws.set_mode(ws.MODE_LTP, niftystocktokens)

# Assign the callbacks.
kws.on_ticks = on_ticks
kws.on_connect = on_connect

kws.connect()