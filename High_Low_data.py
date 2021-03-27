from datetime import date, datetime, time
from nsepy import get_history
niftystocks = ["ADANIPORTS", "ASIANPAINT", "AXISBANK", "BAJAJ-AUTO", "BAJAJFINSV", "BAJFINANCE", "BHARTIARTL", "BPCL",
               "BRITANNIA", "CIPLA", "COALINDIA", "DRREDDY", "EICHERMOT", "GAIL", "GRASIM", "HCLTECH", "HDFC",
               "HDFCBANK", "HEROMOTOCO", "HINDALCO", "HINDUNILVR", "IBULHSGFIN", "ICICIBANK", "INDUSINDBK",
               "INFY", "IOC", "ITC", "JSWSTEEL", "KOTAKBANK", "LT", "M&M", "MARUTI", "NTPC", "ONGC", "POWERGRID",
               "RELIANCE", "SBIN", "SUNPHARMA", "TATAMOTORS", "TATASTEEL", "TCS", "TECHM", "TITAN", "ULTRACEMCO", "UPL",
               "VEDL", "WIPRO", "YESBANK", "ZEEL"]
def tendayshigh(stock_name):
   start1 = datetime.strptime("2019-04-02", "%Y-%m-%d").date()
   end1 = datetime.strptime("2019-04-15", "%Y-%m-%d").date()

   sbin = get_history(symbol=stock_name,
                  start=start1,
                  end=end1)
   sbin=sbin.reset_index()
   return max(sbin.High)

def fivedayshigh(stock_name):
   start1 = datetime.strptime("2019-04-09", "%Y-%m-%d").date()
   end1 = datetime.strptime("2019-04-15", "%Y-%m-%d").date()

   sbin = get_history(symbol=stock_name,
                  start=start1,
                  end=end1)
   sbin=sbin.reset_index()
   return max(sbin.High)

def tendayslow(stock_name):
   start1 = datetime.strptime("2019-04-02", "%Y-%m-%d").date()
   end1 = datetime.strptime("2019-04-15", "%Y-%m-%d").date()

   sbin = get_history(symbol=stock_name,
                  start=start1,
                  end=end1)
   sbin=sbin.reset_index()
   return min(sbin.Low)

def fivedayslow(stock_name):
   start1 = datetime.strptime("2019-04-09", "%Y-%m-%d").date()
   end1 = datetime.strptime("2019-04-15", "%Y-%m-%d").date()

   sbin = get_history(symbol=stock_name,
                  start=start1,
                  end=end1)
   sbin=sbin.reset_index()
   return min(sbin.Low)


tendays_high=[]
fivedays_high=[]
tendays_low=[]
fivedays_low=[]
for i in range(49):
    tendays_high.append(tendayshigh(niftystocks[i]))
    fivedays_high.append(fivedayshigh(niftystocks[i]))
    tendays_low.append(tendayslow(niftystocks[i]))
    fivedays_low.append(fivedayslow(niftystocks[i]))

print("tendays_high")
print(tendays_high)
print("fivedays_high")
print(fivedays_high)
print("tendays_low")
print(tendays_low)
print("fivedays_low")
print(fivedays_low)
