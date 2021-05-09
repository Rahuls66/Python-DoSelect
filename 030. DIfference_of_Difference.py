#30. Difference of Difference

import pandas as pd

l1 = list(map(int, input().split()))
ser = pd.Series(l1)

print(list(ser.diff().values))
print(list(ser.diff().diff().values))

'''
Expected Output:
2 4 6 8 10 12 14 16
[nan, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0]
[nan, nan, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
'''
