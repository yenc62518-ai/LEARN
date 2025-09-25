import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('california_cities.csv')
longd = data.longd
latd = data.latd
population = data.population_total
size = data.area_total_km2

fig, ax = plt.subplots(figsize = (5,5))
cali = ax.scatter(longd, latd, c = np.log10(population), s = population/100, cmap = 'viridis', alpha = 0.5)

ax.set(title = 'phan bo dan so Cali',
       xlabel = 'kinh do',
       ylabel = 'vi do') 

plt.colorbar(cali, label = 'population size')

area_range = [100,200,300,400,500]

for area in area_range:
    plt.scatter([], [], s=area, label = str(area) + 'km$^2$')

plt.legend(labelspacing = 1)

plt.show()