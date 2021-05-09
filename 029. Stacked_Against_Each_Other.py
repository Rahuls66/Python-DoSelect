#29. Stacked against Each Other

import pandas as pd

l1 = input().split()
l2 = input().split()

print(pd.concat([pd.Series(l1), pd.Series(l2)], axis = 1))

'''
Expecte Output:
0 1 2 3
a b c d e
     0  1
0    0  a
1    1  b
2    2  c
3    3  d
4  NaN  e
'''
