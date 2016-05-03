from matplotlib.finance import quotes_historical_yahoo_ochl
from datetime import date
from datetime import datetime
import pandas as pd
today = date.today()
start = (today.year-1,today.month,today.day)
quotes = quotes_historical_yahoo_ochl('AXP',start,today)
fields = ['date','open','close','high','low','volume']
df = pd.DataFrame(quotes,columns=fields)
date_index = [datetime.strftime(date.fromordinal(int(d)),'%y/%m/%d') for d in df['date']]
df.index = date_index
df = df.drop(['date'],axis=1)
#df.index = date.fromordinal(df['date'])
#print df['15/05/20':'15/06/10'].sort('close',ascending=False)[:5]
#month
tmpdf = df['15/05/20':'15/06/10']
list1 = []
for i in range(0,len(tmpdf)):
    list1.append(int(tmpdf.index[i][3:5]))
tmpdf['month'] = list1
t = tmpdf.groupby('month')['volume'].sum()