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
