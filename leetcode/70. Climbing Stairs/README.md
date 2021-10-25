---
file: "climbing-stairs.py"
name: "70. Climbing Stairs"
src: "https://leetcode.com/problems/climbing-stairs/"
tags:
  - Math
  - Dynamic Programming
  - Memoization
done: true
date: 2021-10-24
---

# Climbing Stairs

```text
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?


Example 1:
    Input: n = 2
    Output: 2
    Explanation: There are two ways to climb to the top.
    1. 1 step + 1 step
    2. 2 steps

```

## 정답 코드

```python
class Solution:
    # n 값에 따른 경우의 수
    # n = 1 -> 1개
    # n = 2 -> 2개
    # n = 3 -> 3개
    # n = 4 -> 5개
    # ...
    # f(n) = f(n-1)+f(n-2)
    def climbStairs(self, n: int) -> int:
        dp = [0, 1, 2]

        for i in range(3,n+1):
            dp.append(dp[i-1]+dp[i-2])
        return dp[n]
```

## 다른 사람이 풀이한 코드

아래코드가 더 파이썬 다운 코드 같다. 공간복잡도가 O(1)이며 속도또한 위 코드보다 훨씬 빠르다..!

```python
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <3:
            return n

        p0 = 1
        p1 = 2

        for i in range(3, n+1):
            p0, p1 = p1, p1+p0

        return p1
```
