---
file: "18258.py"
name: "큐 2"
src: "https://www.acmicpc.net/problem/18258"
tags: 
  - 자료 구조
  - 큐
done: true
draft: false
level: 7
difficulty: "Silver IV"
date: 2021-10-20
---

# 큐 2

## deque를 이용해 구현한 코드

```python
from collections import deque
import sys

input = sys.stdin.readline

class Queue:
    def __init__(self) -> None:
        self.queue = deque()

    def push(self, num):
        self.queue.append(num)

    def pop(self):
        return self.queue.popleft() if not self.empty() else -1

    def size(self):
        return len(self.queue)

    def empty(self):
        return True if self.size() < 1 else False

    def front(self):
        return -1 if self.empty() == True else self.queue[0]

    def back(self):
        return -1 if self.empty() == True else self.queue[-1]



s = Queue()
n = int(input())

for i in range(n):
    cmd = input().split()

    if cmd[0] == "push":
        s.push(int(cmd[1]))
    elif cmd[0] == "pop":
        print(s.pop())
    elif cmd[0] == "size":
        print(s.size())
    elif cmd[0] == "empty":
        print(1 if s.empty() else 0)
    elif cmd[0] == "front":
        print(s.front())
    elif cmd[0] == "back":
        print(s.back())
```
