# %%

from utils import load
import matplotlib.pyplot as plt

tick_data = load('./DAT_ASCII_GBPUSD_T_201912.csv')

del tick_data['rand']

print(tick_data.head())

tick_data.plot(title='TickData', y='usd', color='Red')
plt.xlabel('Ticks')
plt.ylabel('Price')

# %%


minute_data = load('./minute.csv')

print(minute_data.head())

minute_data.plot(title='MinuteData', y='Close', x='Date', color='Yellow')
plt.xlabel('Date')
plt.ylabel('Price')

# %%


day_data = load('./day.csv')

print(day_data.head())

day_data.plot(title='DayData', y='Close', x='Date', color='Green')
plt.xlabel('Day')
plt.ylabel('Price')


# %%
