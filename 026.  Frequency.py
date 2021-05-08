#27. Frequency

import pandas as pd
import numpy as np

l1 = input().split()
print(pd.Series(l1).value_counts().sort_index())

'''
Expected Output:
 2 2 2 2 2 2 2 2 2 1 1 1 1 3 3 3 3 3 3 3 4 4 4 4 4
1    4
2    9
3    7
4    5
dtype: int64
'''
