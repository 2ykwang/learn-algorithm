---
file: "1085.md"
name: "직사각형에서 탈출"
src: "https://www.acmicpc.net/problem/1085"
tags:
  - 기하학
  - 수학
done: true
draft: false
level: 3
difficulty: "Bronze III"
date: 2021-11-06
---

# 직사각형에서 탈출

```python
import sys

def input(): return sys.stdin.readline().rstrip()
x, y, w, h = map(int, input().split())
print(min([x, y, w-x, h-y]))
```
