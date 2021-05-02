l1 = [1, 7, 90, 33, 67, 56, 20, 39, 10, 30]

def max_out(l1):
    T = int(input())
    l2 = []
    for i in range(T):
        a,b,c = map(int, input().split())
        k = max(l1[a], l1[b], l1[c])
        l2.append(k)
    for i in l2:
        print(i, end = "\n")

max_out(l1)

'''
Expected Output:
2
1 2 3
4 6 8
90
67
'''
