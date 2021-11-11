
"""
    문제 이름: 수 찾기
    문제 번호: 1920
    문제 링크: https://www.acmicpc.net/problem/1920
    난이도: Silver IV
    태그: 이분 탐색
"""
import sys

def input(): return sys.stdin.readline().rstrip()

_, N = input(), set([int(x) for x in input().split()])
_, M = input(), [int(x) for x in input().split()]

for i in M:
    print('1' if i in N else '0')