import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv('D:\\Code C\\VS\\PRACTICE\\MATPLOTLIB_PRATICE\\temperature_data.tsv', sep = '\t')
data['Date'] = data['Date'].apply(lambda x : x.replace('2025-07-', ''))
fig, ax = plt.subplots(2,2)
mean_day = np.mean(data.Day_Temp)
mean_night = np.mean(data.Night_Temp)

ax[0,0].plot(data.Date, data.Day_Temp, label = 'day', color = 'red')
ax[0,0].set(title = 'nhiet do ban ngay',
            xlabel = 'thang 7',
            ylabel = 'nhiet do')
ax[0,0].plot(data.Night_Temp, label = 'night', color = 'blue')
ax[0,0].grid(True)
             

ax[0,1].bar(['Day avg', 'Night avg'], [mean_day, mean_night], color = ['red', 'blue'])
ax[0,1].set(title = 'nhiet do trung binh',
            xlabel = 'ngay',
            ylabel = 'nhiet do')

ax[1,0].hist(data.Day_Temp, bins = 15, color='red', edgecolor='black', alpha=0.7, label='Day Temp')
ax[1,0].legend() 

ax[0,0].legend()
plt.tight_layout()
plt.show()