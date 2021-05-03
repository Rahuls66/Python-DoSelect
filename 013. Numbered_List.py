#13. Numbered List

T = int(input())
for _ in range(T):
    l1 = list(map(int, input().split()))
    sp, ep = l1[0], l1[1]
    if sp < 1:
        print("Out of Range")
    elif ep > 100:
        print("Out of Range") 
    elif len(list(range(sp, ep+1))) != 10:
        print("Difference Not in Range")
    else:
        print(list(range(sp, ep+1)))

'''
Expected Output:
3
1 9
Difference Not in Range
22 31
[22, 23, 24, 25, 26, 27, 28, 29, 30, 31]
90 103
Out of Range
'''
