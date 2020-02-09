from utils import load

# 9
data = load('./day.csv')

print(data['Date'].diff().sort_values(ascending=False)[:10])