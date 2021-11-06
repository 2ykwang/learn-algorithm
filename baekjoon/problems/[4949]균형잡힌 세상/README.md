---
file: "4949.md"
name: "균형잡힌 세상"
src: "https://www.acmicpc.net/problem/4949"
tags:
  - 자료 구조
  - 스택
  - 문자열
done: true
draft: false
level: 7
difficulty: "Silver IV"
date: 2021-11-06
---

# 균형잡힌 세상

```python
import sys

def input(): return sys.stdin.readline().rstrip()

parentheses = {
    ')': '(',
    ']': '[',
}
open_parentheses = parentheses.values()
close_parentheses = parentheses.keys()

def solve(text: str) -> bool:

    # 괄호 갯수가 맞지 않을경우
    st = []
    for c in text:
        # 여는 괄호 일경우 push
        if c in open_parentheses:
            st.append(c)

        elif c in close_parentheses:
            # 닫는괄호 단독으로 나오거나 대응하는 괄호가 매칭되지 않을경우 break
            if len(st) > 0 and st[-1] == parentheses[c]:
                st.pop()
            else:
                return False

    return len(st) == 0


while True:
    text = input()

    if text == '.':
        break

    print("yes" if solve(text) else "no" )

# 108ms
```
