#16. Basic Calculator

T = int(input())
a, b = map(int, input().split())

for _ in range(T):
    op = input()
    if op == '+':
        print(a+b)
    elif op == '-':
        print(a-b) 
    elif op == '*':
        print(a*b)
    elif op == '/':
        print(int(a/b))
    elif op == '%':
        print(a%b)
    elif op == '//':
        print(a//b)
        
        
'''
Expected Output:
5
20 15
+
35
-
5
*
300
/
1
%
5
'''
