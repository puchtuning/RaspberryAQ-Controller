import json
import time
import pandas as pd
import matplotlib.pyplot as plt



datatime = time.strftime("%Y-%m-%d")
data = {}

data = open("../data/" + datatime + "_data_RaspberryAQ.json")


data = json.load(data)
dates = [i['timestamp'] for i in data["data"]]
values = [i['aq_temp_sen'] for i in data['data']]

df = pd.DataFrame({'dates':dates, 'values':values})
df['dates']  = [pd.to_datetime(i) for i in df['dates']]

x = len(dates)
y = x - 50

i = x -1

while(i>-1):
    datum = dates[i]
    dates[i] = datum[11:16]

    if(i==y):
        break
    elif(i==0):
        y = 0
        break

    i = i-1
    

print(dates[y:x])
print(values[y:x])

plt.plot(dates[y:x], values[y:x])
plt.show()


