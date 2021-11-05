
"""
    문제 이름: 피보나치 함수
    문제 번호: 1003
    문제 링크: https://www.acmicpc.net/problem/1003
    난이도: Silver III
    태그: 다이나믹 프로그래밍
"""
import sys


def input(): return sys.stdin.readline().rstrip()


def solve(num: int) -> tuple:
    DP1 = [1, 0, 1]  # 0
    DP2 = [0, 1, 1]  # 1

    for i in range(3, num+1):
        DP1.append(DP1[i-1]+DP1[i-2])
        DP2.append(DP2[i-1]+DP2[i-2])

    return DP1[num], DP2[num]

for _ in range(int(input())):
    print(*solve(int(input())))