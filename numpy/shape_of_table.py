import numpy as np

a = np.arange(0, 10)

a2 = a[np.newaxis, :]

print(a.shape)
print(a)
print(a2.shape)
print(a2)
