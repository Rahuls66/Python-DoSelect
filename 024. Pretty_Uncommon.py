#24. Pretty Uncommon *** 1 TEST CASE PASSING ONLY

import pandas as pd
import warnings
warnings.filterwarnings('ignore')

list1 = map(int, input().split())
list2 = map(int, input().split())

series1 = pd.Series(list((list1)))
series2 = pd.Series(list((list2)))

l = pd.Series(list(set(series1.append(series2))), dtype = object)
k1 = l[~(l.isin(series1))]
k2 = l[~(l.isin(series2))]

print(k2.append(k1))

'''
Expected output:
1 2 3 4 5 6
4 5 6 7 8 9
0    1
1    2
2    3
6    7
7    8
8    9
dtype: object
'''
