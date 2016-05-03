import pandas as pd
data = pd.read_table('./ml-100k/u.data',sep='\t',names = None)
user = pd.read_table('./ml-100k/u.user',sep='|',names = None)
item = pd.read_table('./ml-100k/u.item',sep='|',names = None)
m = pd.merge(data.drop(['timestamp'],axis=1),user.drop(['age','occupation','zip code'],axis=1))
mm = m.groupby('item-id').std()
mm.plot()