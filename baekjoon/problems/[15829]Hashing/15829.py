
"""
    문제 이름: Hashing
    문제 번호: 15829
    문제 링크: https://www.acmicpc.net/problem/15829
    난이도: Bronze II
    태그: 해싱
"""
import sys

def input(): return sys.stdin.readline().rstrip()

# input()
# values = [(ord(c)-ord('a')+1)*(31**idx) for idx, c in enumerate(input())]
# print(sum(values))
input(), print(sum([(ord(c)-97+1)*(31**i)
                    for i, c in enumerate(input())]) % 1234567891)
