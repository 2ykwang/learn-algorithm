---
file: "2960.py"
name: "에라토스테네스의 체"
src: "https://www.acmicpc.net/problem/2960"
tags: 
  - 구현
  - 수학
  - 정수론
  - 소수 판정
  - 에라토스테네스의 체
done: true
draft: false
level: 7
difficulty: "Silver IV"
date: 2021-11-02
---
# 에라토스테네스의 체

```python
import sys


def input(): return sys.stdin.readline().rstrip()


def solve(n, k):
    arr = [True for _ in range(n+1)]
    idx = 0

    for i in range(2, n + 1):
        for j in range(i, n + 1, i):
            if arr[j]: 
                arr[j] = False
                idx += 1
                if idx == k:
                    return j
    return -1


n, k = map(int, input().split())

print(solve(n, k))
```