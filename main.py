#telegram-send links 
#https://pypi.org/project/telegram-send/#installation
#https://medium.com/@robertbracco1/how-to-write-a-telegram-bot-to-send-messages-with-python-bcdf45d0a580


from nsetools import Nse
import pandas as pd
from pprint import pprint
import pandas as pd
import telegram_send
nse=Nse()

Gainers=nse.get_top_gainers()
#print(Gainers)
#telegram_send.send(messages=Gainers)
df = pd.DataFrame(Gainers)
Gainer_send = df.drop(df.columns[[1, 2,3,4, 6,8,9,10,11]], axis = 1, inplace = True)
print(Gainer_send)
print(df)
a=str(df)
print(a)
telegram_send.send(messages=[a])

#
#

#Gainers=pd.DataFrame(Gainers)

#Losers=nse.get_top_losers()
#Losers=pd.DataFrame(Losers)
#print(Losers.values)


#BUY=[x for x in Gainers['symbol']]
#SELL=[x for x in Losers['symbol']]
#print('Gainers')
#for x in range(len(BUY)):
#    print(BUY[x])
#print('losers')
#for x in range(len(SELL)):
#    print(SELL[x])

#send msg
#telegram_send.send(messages=["Wow that was easy''!"])


