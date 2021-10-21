---
file: "10828.py"
name: "스택"
src: "https://www.acmicpc.net/problem/10828"
tags:
  - 스택
  - 자료구조
done: true
---

# 스택

`stdin readline()`을 꼭 쓰자.

## 정답 코드

```python
import sys

class Stack:
    def __init__(self) -> None:
        self.stack = []

    def push(self, num):
        self.stack.append(num)

    def size(self):
        return len(self.stack)

    def empty(self):
        return True if self.size() < 1 else False

    def top(self):
        return -1 if self.empty() == True else self.stack[-1]

    def pop(self):
        result = self.top()
        if result != -1:
            del self.stack[-1]
        return result


s = Stack()

n = int(input())

for i in range(n):
    cmd = sys.stdin.readline().rstrip().split()

    if cmd[0] == "push":
        s.push(int(cmd[1]))
    elif cmd[0] == "pop":
        print(s.pop())
    elif cmd[0] == "size":
        print(s.size())
    elif cmd[0] == "empty":
        print(1 if s.empty() else 0)
    elif cmd[0] == "top":
        print(s.top())

```
