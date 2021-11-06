
"""
    문제 이름: 소수 구하기
    문제 번호: 1929
    문제 링크: https://www.acmicpc.net/problem/1929
    난이도: Silver II
    태그: 수학, 정수론, 소수 판정, 에라토스테네스의 체
"""
import sys


def input(): return sys.stdin.readline().rstrip()


def is_prime(m: int, n: int) -> bool:
    if n <= 1:
        return []

    l = n-m+1
    prime = [True] * l

    for i in range(2, int(n**0.5)+1):
        for j in range(2*i, n+1, i):
            if j-m >= 0 and prime[j-m]:
                prime[j-m] = False

    return [x+m for x in range(2-m if m <= 2 else 0, l) if prime[x]]
    # return not any([num % i == 0 for i in range(2, int(num**0.5)+1)])


nums = is_prime(*map(int, input().split()))
for n in nums:
    print(n)

# 948ms
