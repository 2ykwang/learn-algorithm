---
file: "10866.py"
name: "덱"
src: "https://www.acmicpc.net/problem/10866"
tags: 
  - 자료 구조
  - 덱
done: true
draft: false
level: 7
difficulty: "Silver IV"
date: 2021-10-21
---

# 덱

## 정답 코드

```python
from collections import deque
import sys

def input(): return sys.stdin.readline().rstrip()

queue = deque()

n = int(input())

for _ in range(n):
    cmd = input().split()

    if cmd[0] == "push_front":
        queue.appendleft(int(cmd[1]))
    elif cmd[0] == "push_back":
        queue.append(int(cmd[1]))
    elif cmd[0] == "pop_front":
        print(queue.popleft() if len(queue) > 0 else -1)
    elif cmd[0] == "pop_back":
        print(queue.pop() if len(queue) > 0 else -1)
    elif cmd[0] == "size":
        print(len(queue))
    elif cmd[0] == "empty":
        print(1 if len(queue) == 0 else 0)
    elif cmd[0] == "front":
        print(queue[0] if len(queue) > 0 else -1)
    elif cmd[0] == "back":
        print(queue[-1] if len(queue) > 0 else -1)
```
