import numpy as np

numerator_list = [1, 1]
denominator_list = [2, 2]

lcm = np.lcm.reduce(denominator_list)

for idx, i in enumerate(numerator_list):
        x = lcm / denominator_list[idx]
        numerator_list[idx] = (x * i)


print lcm    
print numerator_list