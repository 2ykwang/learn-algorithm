---
file: "1003.md"
name: "피보나치 함수"
src: "https://www.acmicpc.net/problem/1003"
tags: 
  - 다이나믹 프로그래밍
done: true
draft: false
level: 8
difficulty: "Silver III"
date: 2021-11-06
---
# 피보나치 함수

```text
0               0
1               1
10              2
101             3
10110           4
10110101        5
```

규칙을 보자

```python
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
```
