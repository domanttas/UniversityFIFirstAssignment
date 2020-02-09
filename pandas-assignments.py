import numpy as np
import pandas as pd
import datetime

dates = pd.date_range('20190214', periods=6)
numbers = np.matrix([[101, 103], [105.5, 75], [102, 80.3],
                     [100, 85], [110, 98], [109.6, 125.7]])

df = pd.DataFrame(numbers, index=dates, columns=['A', 'B'])

print(df)
print('#####')

# 1
print('##### 1')
print(df.loc['2019-02-18'])

# 2
print('##### 2')
print(df.loc[datetime.datetime(2019,2,18)])

# 3
print('##### 3')
print(df.iloc[-2])

# 4
print('##### 4')
print(df.head(2)['B'])

# 5
print('##### 5')
print(df.sort_values('B', ascending=False))

# 6
print('##### 6')
print(df.max()['A'])

# 7
print('##### 7')
df.replace([df['A'].max()], df['A'].max() * 2, inplace=True)
print(df)

# 8
print('##### 8')
print(df[df['A'] > 105])

#10
print('##### 10')
print(df[df['A']>df['B']])
# Jupyter notebooks

#%%
import numpy as np
import pandas as pd
import datetime

dates = pd.date_range('20190214', periods=6)
numbers = np.matrix([[101, 103], [105.5, 75], [102, 80.3],
                     [100, 85], [110, 98], [109.6, 125.7]])

df = pd.DataFrame(numbers, index=dates, columns=['A', 'B'])
df.replace([df['A'].max()], df['A'].max() * 2, inplace=True)
#%%

# 9
print('##### 9')
df['A'].plot()

# %%
