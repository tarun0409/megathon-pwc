from keras.models import load_model
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import time
import datetime
from datetime import date

model = load_model('three_layer_high_large.h5')
num_days = 7
np.random.seed(seed=10004)
df = pd.read_csv('drainage_data_high_large.csv')
df.columns=['Date','Gas','Flow','Level','Temperature','Label']
x = df[['Gas','Flow','Level','Temperature']]
y = df[['Label']]
y_arr = y.to_numpy()
y_arr = np.reshape(y_arr,(y_arr.shape[0],))
y_arr = y_arr - 1
y_data = np.zeros((y_arr.shape[0], 4))
y_data[np.arange(y_arr.shape[0]), y_arr] = 1
x_np = x.to_numpy()
x_np = x_np - x_np.mean()
x_np = x_np/x_np.max()
x_new = np.reshape(x_np,(int(x_np.shape[0]/5),5,x_np.shape[1]))    
y_new = np.reshape(y_data,(int(y_data.shape[0]/5),5,y_data.shape[1]))
master_array = list()
index = list()
today = date.today()
x_ticks = list()
tick_labels = list()
x_dates = list()
for i in range(0,num_days):
    today += datetime.timedelta(days=1)
    x_dates.append(today)
    d = today.strftime("%d/%m/%Y")
    x_ticks.append(d)
index = [1,2,3,4,5,6,7]
master_array = [0,0,0,0,0,0,0]
curr_index = 7
beg = 0
end = 7

x = x_dates[beg:end]
y = master_array[beg:end]
plt.ion()
fig = plt.figure()
ax = fig.add_subplot(111)

plt.ylim((0, 5))
plt.xlim((x_dates[beg],x_dates[end-1]))
fig.autofmt_xdate()
line1, = ax.plot(x, y, 'r-')
for i in range(0,x_new.shape[0]):
    inp = x_new[i].reshape(1,x_new[i].shape[0],x_new[i].shape[1])
    results = model.predict_classes(inp)
    results+=1
    add_list = list(results[0])
    l = len(add_list)
    for i in range(l):
        curr_index+=1
        today += datetime.timedelta(days=1)
        d = today.strftime("%d/%m/%Y")
        x_dates.append(today)
        index.append(curr_index)

    master_array.extend(add_list)
    line1.set_xdata(x_dates[beg:end-1])
    line1.set_ydata(master_array[beg:end-1])
    fig.canvas.draw()
    fig.canvas.flush_events()
    end+=1
    beg+=1
    plt.xlim((x_dates[beg],x_dates[end-1]))
    
    time.sleep(2)
    