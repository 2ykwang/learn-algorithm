---
file: "1874.md"
name: "스택 수열"
src: "https://www.acmicpc.net/problem/1874"
tags: 
  - 자료 구조
  - 스택
done: true
draft: false
level: 8
difficulty: "Silver III"
date: 2021-10-21
---

# 스택 수열

처음 문제를 봤을때 내용이 이해가 안됐는데 n개의 수를 가진 수열이 주어졌을 때 1부터 n까지의 수를 스택에 push, pop을 하여 똑같은 수열을 만들 수 있는지 판별하는 코드를 만드는 문제였다. 1부터 n의 숫자를 push 하는 순서는 반드시 `오름차순`이어야 한다. push 할 경우 `+` pop 할경우 `-`를 출력한다. 만들 수 없는 수열일 경우 `NO`를 출력한다.

## 정답 코드

```python
import sys

def input(): return sys.stdin.readline().rstrip()

n = int(input())
nums = [int(input()) for i in range(n)]

st = []
answer = []
cur = 0
for num in nums:
    # cur이 num과 같을 때 까지 push
    while cur < num:
        cur += 1
        st.append(cur)
        answer.append("+")
    # 스택 마지막요소가 num 일경우 pop
    if st[-1] == num:
        st.pop()
        answer.append("-")
        continue
    else:
        # 스택 마지막요소가 num이 아닐경우 만들어질 수 없는 수열
        # ex [1 2 3] 인데 숫자 4가 올경우
        print("NO")
        break

# 수를 모두 사용하여 스택이 비워져 있을 경우에만 출력해준다.
if len(st) == 0:
    print('\n'.join(answer)) 
```
