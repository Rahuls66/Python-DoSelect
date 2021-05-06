#17. Prime Paramters


T = int(input())

def isPrime(num):
    if num > 1:   
        for i in range(2, num):
            if num % i == 0:     
                print("COMPOSITE")
                break         
        else:
            print("PRIME")   
        

for _ in range(T):
    num = int(input())
    if (2 <= num <= 1000) is not True or (1 <= T <= 100) is not True:                                 
        print("Out of Range") 
    else:
        isPrime(num)
        
'''
Expected Output
3
1
Out of Range
7
PRIME
9
COMPOSITE
'''
