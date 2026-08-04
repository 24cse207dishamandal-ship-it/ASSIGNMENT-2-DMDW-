print("using logic:")
data = [10, 12, 15, 18, 20, 20, 22, 25]
mean = sum(data) / len(data)
variance = 0
for i in data:
    variance += (i - mean) ** 2
variance = variance / len(data)
print("variance =", variance)
print("using library function:")
import numpy as np
print("variance:",np.var(data))

