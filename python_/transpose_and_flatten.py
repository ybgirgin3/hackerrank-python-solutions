import numpy as np
n,m = map(int, input().split())

arr = np.array([input().split() for _ in range(n)], int)

print(arr.T)
#print(arr.flatten)
print(arr.flatten())
