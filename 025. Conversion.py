#25. Conversion*** 1 Test Case Failed

import numpy as np
import pandas as pd

m, n = map(int, input().split())
l1 = list(map(int, input().split()))
arr1 = np.array(l1)

if (m*n == len(l1)) and (m >= 2) and (n <= 10):
    print(pd.DataFrame(arr1.reshape(m,n)))
else:
    print("Weird Order!")
    
'''
Expected Output:
2 3
1 2 3 4 5 6 7 8
Weird Order!
'''
