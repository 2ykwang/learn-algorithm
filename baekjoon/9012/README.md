---
file: "9012.py"
name: "괄호"
src: "https://www.acmicpc.net/problem/9012"
tags:
  - 문자열
  - 스택
  - 자료구조
done: false
---

# 괄호

## 정답 코드

```python
n = int(input())

for i in range(n):
    ps = input()
    #현재 괄호 깊이
    deps = 0
    for chr in ps:
        # 괄호 열면 deps + 1
        if chr == '(':
            deps += 1
        # 괄호 닫으면 deps - 1
        elif chr == ')':
            deps -= 1
        # 괄호 연것보다 닫는게 많을경우 break
        if deps < 0:
            break
    # 최종적으로 괄호의 깊이가 0이 돼야 괄호 문자열이 된다.
    print("YES" if deps==0 else "NO")
```
