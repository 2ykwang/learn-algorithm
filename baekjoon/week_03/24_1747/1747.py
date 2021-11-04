import sys
import math

def input(): return sys.stdin.readline().rstrip()

def is_palindrome(text: str) -> bool: 
    text_len = len(text)
    mid = text_len//2

    for i in range(mid):
        if text[i] is not text[text_len-i-1]:
            return False
    return True

def is_prime(num: int) -> bool:
    if num <= 1:
        return False
    for i in range(2, int(math.sqrt(num))+1):
        if num%i == 0:
            return False
    return True 

maximum = 1003002

n = int(input()) 
for i in range(n, maximum):
    if is_prime(i) and is_palindrome(str(i)):
        print(i)
        break