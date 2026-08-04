print("using logic:")
import math
data = [10, 12, 15, 18, 20, 20, 22, 25]
mean = sum(data) / len(data)
variance = 0
for i in data:
    variance += (i - mean) ** 2
variance = variance / len(data)
std = math.sqrt(variance)
print("Standard Deviation :", std)
print("using library function:")
import numpy as np
print("Standard deviation:",np.std(data))

