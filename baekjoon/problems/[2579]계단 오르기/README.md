---
file: "2579.md"
name: "계단 오르기"
src: "https://www.acmicpc.net/problem/2579"
tags:
  - 다이나믹 프로그래밍
done: false
draft: false
level: 8
difficulty: "Silver III"
date: 2021-11-06
---

# 계단 오르기

```python
# 1. 계단은 한 번에 한 계단씩 또는 두 계단씩 오를 수 있다. 즉, 한 계단을 밟으면서 이어서 다음 계단이나, 다음 다음 계단으로 오를 수 있다.
# 2. 연속된 세 개의 계단을 모두 밟아서는 안 된다. 단, 시작점은 계단에 포함되지 않는다.
# 3. 마지막 도착 계단은 반드시 밟아야 한다.
# 계단은 300 이하 자연수
import sys

def input(): return sys.stdin.readline().rstrip()

n = int(input())

stairs = [int(input()) for _ in range(n)]
DP = [0] * n
# DP[n] - > n 계단까지 올라갔을떄 가장 높은 점수 값.
DP[0] = stairs[0]
DP[1] = stairs[0] + stairs[1]
DP[2] = max(stairs[0] + stairs[2], stairs[1] + stairs[2])

for i in range(3, n):
    DP[i] = max(DP[i-3]+stairs[i-1]+stairs[i],  DP[i-2] + stairs[i])

print(DP[-1])
# for i in range(stairs):
#     dp[i] = max(dp[i+1,i-2])
```
