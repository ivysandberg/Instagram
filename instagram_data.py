import numpy as np
import pandas as pd
import json
import matplotlib.pyplot as plt
import csv

""" import follower data """

path = '/Users/ivysandberg/MyData/ivysandberg_20190104/connections.json'

# import using read_json
#data = pd.read_json(path)

#df = pd.DataFrame(data)
#followers_bydate = df.sort_values('followers')
#print (followers_bydate)


# reading the JSON data using json.load()
with open(path) as data:
    dict_data = json.load(data)

# converting json dataset from dictionary to dataframe
d2 = pd.DataFrame.from_dict(dict_data)#, orient='index')
d2['index1'] = d2.index
d3=d2[['index1', 'followers']]
#print (d3)
#print (type(d3))

# restructure dataframe (make username a column not an index)
d3 = d3.reset_index()
d3 = d3.drop(['index'], axis=1)
d3 = d3.rename(columns={'index1': 'username', 'followers': 'date'})

#print(d3)
#print (d3.columns)
follower_df = d3    # renaming d3
#print (follower_df)

""" import media data """

path2 = '/Users/ivysandberg/MyData/ivysandberg_20190104/media.json'


with open(path2) as data_file:
    data2 = json.load(data_file)
    #print (data2)


# restructure DataFrame
df2 = pd.DataFrame.from_dict(data2, orient='index')
df2.reset_index(level=0, inplace=True)
df2=df2.drop([0], axis=1)
df2=df2.transpose()

#print(list(df2.columns))
#print (df2)

''' extract just the data on instgram stories from the media data '''
df3=df2[0]  # extracts just stories (format: list of dictionaries)
#print(df3)

'''parse string into list'''
var1=df3[1]
#print(var1)

#print(type(var1))
#print(var1.keys())



'''convert keys to column names'''
cap=[]  # caption
tak=[]  # taken_at
pat=[]  # path
newdf = pd.DataFrame()
for i in range(1,195):
    cp = df3[i]['caption']
    tk = df3[i]['taken_at']
    pt = df3[i]['path']
    cap.append(cp)
    tak.append(tk)
    pat.append(pt)
newdf['caption']=cap
newdf['date']=tak
newdf['path']=pat
#print(newdf)

my_posts=newdf['caption']
#print (list(my_posts))

'''Merging data
pd.merge(left=DataFrame, right=DataFrame, on=None, left_on=‘left column name’, right_on=‘right column name’)
'''

#newdf=newdf.merge(d3, how='outer') # outer join
#print(newdf)


''' export dataframes as csv'''

d3.to_csv('/Users/ivysandberg/MyData/instadata.csv', index=False, header=False)
newdf.to_csv('/Users/ivysandberg/MyData/instastorydata.csv', index=False, header=False)
