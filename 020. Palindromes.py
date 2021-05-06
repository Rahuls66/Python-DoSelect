#20. Palindromes

def isPalindrome(s):
        if s[:] == s[::-1]:
            print("String is a PALINDROME")
        else:
            print("String NOT a PALINDROME")
            
s = input().lower()
if s == s.replace(" ", ""):
    isPalindrome(s)
else:
    print("String NOT a PALINDROME")
    
'''
Expected Output:
EveDamnedEdenMadEve
String is a PALINDROME
'''
