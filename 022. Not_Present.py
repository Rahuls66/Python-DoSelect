#22. Not Present

import pandas as pd

list1 = list(map(int, input().split()))
list2 = list(map(int, input().split()))

series1 = pd.Series(list1, dtype = 'object')
series2 = pd.Series(list2, dtype = 'object')

print (series1[~(series1.isin(series2))])

'''
Expected Output:
1 4 3 4 1
1 2 3 4
0    1
1    4
2    3
3    4
4    1
0    1
1    2
2    3
3    4
dtype: object
'''
