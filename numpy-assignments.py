import numpy as np

# 1
print('##### 1')
a = np.random.randint(low=1, high=10, size=10)
b = np.random.randint(low=1, high=10, size=10)

print(a)
print(b)

print(sum(a+b))

# 2
print('##### 2')
a = np.random.randint(low=-10, high=10, size=10)

a[a > 0] = 0
print(a)

# 3
print('##### 3')
a = np.random.randint(low=1, high=10, size=10)

print(a)

result = a[a <= 6]
print(result)

# 4
print('##### 4')
a = np.random.randint(low=1, high=10, size=10)

print(a)

uniques, count = np.unique(a, return_counts=True)
print(uniques[count > 1])

# 5
print('##### 5')
a = np.random.randint(low=1, high=10, size=10)
b = np.random.randint(low=1, high=10, size=10)

print(a)
print(b)

print(a[np.greater(a, b) == True])

# 6
print('##### 6')
a = np.random.randint(low=1, high=10, size=10)

print(a)

last = a[-1::]
a = np.roll(a, -1)
a = np.append(a, last)

print(a)

# 7
print('##### 7')
a = np.random.randint(low=1, high=10, size=10)

print(a)

a = np.flip(a, 0)

print(a)

# 8
print('##### 8')
a = np.random.randint(low=1, high=10, size=10)

print(a)

a[1::2] = 0

print(a)

# 9
print('##### 9')
a = np.random.randint(10, size=(3, 3))

print(a)

# rows
print(a.mean(1))
# cols
print(a.mean(0))

# 10
print('##### 10')
a = np.random.randint(10, size=(3, 3))

print(a)

a = np.diagonal(np.flip(a, 1))
print(np.flip(a))
