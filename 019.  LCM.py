#19. Least Common Multiple

def LCM(a, b):
    if a > b:
        grt = a
    else:
        grt = b
        
    while True:
        if (grt % a == 0) and (grt % b == 0):
            lcm = grt
            break
        grt += 1
    print(lcm)

T = int(input())   
for _ in range(T):
    a,b = map(int, input().split())
    if (1 <= a <= 1000) and (1 <= b <= 1000):
        LCM(a,b)
    else:
        print("Out of Range!")
        
'''
Expected Output:
3
1 5
5
21 28
84
999 1008
Out of Range!
'''
