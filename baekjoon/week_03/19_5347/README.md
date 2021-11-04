---
file: "5347.md"
name: "LCM"
src: "https://www.acmicpc.net/problem/5347"
tags: 
  - 유클리드 호제법
  - 수학
  - 정수론
done: true
draft: false
level: 7
difficulty: "Silver IV"
date: 2021-11-02
---
# LCM

```python
import sys

def input(): return sys.stdin.readline().rstrip()


def LCM(a, b):
    def GCD(a, b):
        while b:
            a, b = b, a % b
        return a
    # lcm = a * b / 최대공약수
    return int(a * b / GCD(a, b))


n = int(input())

for i in range(n):
    a, b = map(int, input().split())
    print(LCM(a, b))
```