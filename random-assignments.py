#%%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Generating dates
dates = np.arange('2018-01', '2018-12', dtype='datetime64[D]')

# Generating closed price
prices = np.random.uniform(low=30, high=35, size=(dates.size))

# Creating data frame
data = pd.DataFrame({'Date': dates, 'Close': prices})

print(data.head())

# Plotting
data.plot(title='RandomData', y='Close', x='Date', color='Black')
plt.xlabel('Day')
plt.ylabel('Price')