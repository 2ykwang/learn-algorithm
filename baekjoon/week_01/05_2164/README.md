---
file: "2164.md"
name: "카드2"
src: "https://www.acmicpc.net/problem/2164"
tags: 
  - 자료 구조
  - 큐
done: true
draft: false
level: 7
difficulty: "Silver IV"
date: 2021-10-20
---

# 카드2

## 정답 코드

```python
from collections import deque
import sys

n = int(sys.stdin.readline())
# 1부터 n까지의 번호를 가진 카드를 만들어 준다
# list comprehension
answer = deque([i for i in range(1, n+1)])

# 카드가 1장이 될 때까지 반복
while len(answer) > 1:
    """
        설명

        4 장의 카드가 있다면
        각각의 카드는 1 2 3 4 의 번호를 갖는다.
        카드를 한장 버린뒤 한장의 카드를 가장 아래로 옮기면
        1 2 3 4 - >
        2 3 4 - >
        3 4 2 가 된다
        코드로 구현하면
        popleft - >
        temp = popleft
        append(temp)

        이 과정을 queue 요소가 단 한개만 남을때 까지 반복한다.
    """
    answer.popleft()
    answer.append(answer.popleft())

print(answer.pop())
```

## 시간 초과 코드

```python
n = int( input())
# n = 6
answer = [i for i in range(1, n+1)]

while len(answer) > 1:
    answer.pop(0)
    answer.append(answer.pop(0))

print(answer[0])
```

### 시간 초과 코드 2

```python
n = int( input())
# n = 6
answer = [i for i in range(1, n+1)]

current_index = 0
while len(answer) > 1:
    answer.pop(current_index)
    current_index += 1
    if current_index >= len(answer):
        current_index = (current_index%len(answer))
print(answer[0])
```
