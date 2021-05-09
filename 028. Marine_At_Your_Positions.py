#28. Marines! At Your Positions!

import pandas as pd

list_input = input().split()
list_pos = list(map(int, input().split()))
print(pd.Series(list_input).iloc[list_pos])

'''
Expected Output:
a b c d e f g h i j k l m n o p q r s t u v w x y z
1    b
2    c
8    i
dtype: object
'''
