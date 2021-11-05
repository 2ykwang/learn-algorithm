---
file: "n-th-tribonacci-number.py"
name: "1137. N-th Tribonacci Number"
src: "https://leetcode.com/problems/n-th-tribonacci-number/"
tags:
  - Math
  - Dynamic Programming
  - Memoization
done: true
draft: false
difficulty: "Easy"
date: 2021-10-24
---

# N-th Tribonacci Number

## 문제

```text
The Tribonacci sequence Tn is defined as follows:

T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

Given n, return the value of Tn.

Input: n = 4
Output: 4
Explanation:
T_3 = 0 + 1 + 1 = 2
T_4 = 1 + 1 + 2 = 4

```

## 정답 코드

```python
class Solution:
    def tribonacci(self, n: int) -> int:
        dp = [0, 1, 1]

        # 크기가 고정된 리스트를 만들필요가 없었다.
        for i in range(3, n+1):
            dp.append(dp[i-3] + dp[i-2] + dp[i-1]);

        return dp[n]
```

## 처음에 짠 코드

```python
class Solution:
    def tribonacci(self, n: int) -> int:
        # 입력받은 n이 2이하면 0 or 1 반환
        if n<=2:
            return 0 if n==0 else 1

        # 0 <= n <= 37
        dp = [0 for _ in range(0,38)]

        for i in range(0, n+1):
            if i<=2:
                dp[i] = 0 if i==0 else 1
            else:
                # Tn+3 = Tn + Tn+1 + Tn+2
                dp[i] = dp[i-3] + dp[i-2] + dp[i-1];

        return dp[n]

```
