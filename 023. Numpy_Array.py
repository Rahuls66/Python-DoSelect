# 23. Numpy Array

import numpy as np

stp = int(input())
enp = int(input())
step = int(input())

if (1 <= stp < enp <= 10**5) and (2 <= step < enp <= 10**5):
    for i in np.arange(stp, enp+1, step):
        print(i)
else:
    print("Constraints are failing!")

'''
Expected output:
2
11
3
2
5
8
11
'''
