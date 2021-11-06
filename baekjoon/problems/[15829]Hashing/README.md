---
file: "15829.md"
name: "Hashing"
src: "https://www.acmicpc.net/problem/15829"
tags:
  - 해싱
done: true
draft: false
level: 4
difficulty: "Bronze II"
date: 2021-11-06
---

# Hashing

```python
import sys

def input(): return sys.stdin.readline().rstrip()

# input()
# values = [(ord(c)-ord('a')+1)*(31**idx) for idx, c in enumerate(input())]
# print(sum(values))
input(), print(sum([(ord(c)-97+1)*(31**i)
                    for i, c in enumerate(input())]) % 1234567891)
```
