
"""
    문제 이름: 계단 오르기
    문제 번호: 2579
    문제 링크: https://www.acmicpc.net/problem/2579
    난이도: Silver III
    태그: 다이나믹 프로그래밍
"""
import sys


def input(): return sys.stdin.readline().rstrip()

def solve(stairs: list, count:int) -> int:
    if count <= 2:
        return sum(stairs)

    DP = [0] * count
    DP[0] = stairs[0]
    DP[1] = stairs[0] + stairs[1]
    DP[2] = max(stairs[0] + stairs[2], stairs[1] + stairs[2])
    for i in range(3, n):
        DP[i] = max(DP[i-3]+stairs[i-1]+stairs[i],  DP[i-2] + stairs[i])
    
    return DP[-1]


n = int(input())

stairs = [int(input()) for _ in range(n)]


print(solve(stairs, n))


# for i in range(stairs):
#     dp[i] = max(dp[i+1,i-2])
