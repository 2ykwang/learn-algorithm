---
file: "1920.md"
name: "수 찾기"
src: "https://www.acmicpc.net/problem/1920"
tags:
  - 이분 탐색
done: true
draft: false
level: 7
difficulty: "Silver IV"
date: 2021-11-12
---

# 수 찾기

## 풀이 코드

```python
import sys

def input(): return sys.stdin.readline().rstrip()

_, N = input(), set([int(x) for x in input().split()])
_, M = input(), [int(x) for x in input().split()]

for i in M:
    print('1' if i in N else '0')
```
