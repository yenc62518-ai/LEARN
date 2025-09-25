import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

c_df = sns.load_dataset('tips')
sns.set_theme(style = 'whitegrid')
print(c_df.head())
sns.displot(data = c_df, x = 'total_bill', col = 'time', kde = True)
plt.show()