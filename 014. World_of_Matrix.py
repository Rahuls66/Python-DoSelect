#14. World of Matrix

T = int(input())
for _ in range(T):
    N = int(input())
    if N % 3 == 0:
        if N % 2 == 0:
            print('Zion')
        else:
            print("Matrix")
    else:
        if N % 2 == 0:
            print('Reality')
        else:
            print("Glitch") 
            
            
'''
Expected Output:
6
2
Reality
3
Matrix
4
Reality
5
Glitch
6
Zion
7
Glitch
'''
