---
file: "10799.py"
name: "쇠막대기"
src: "https://www.acmicpc.net/problem/10799"
tags: 
  - 자료 구조
  - 스택
done: true
draft: false
level: 8
difficulty: "Silver III"
date: 2021-10-21
---

# 쇠막대기

## 정답 코드

```python
stick = input()

answer = 0
# 현재 괄호 깊이
deps = 0

for i in range(len(stick)):
    # 괄호 열면 deps + 1 닫으면 -1
    deps += 1 if stick[i] == '(' else -1

    if stick[i] == '(':
        if i+1 < len(stick) and stick[i+1] == ')':
            # 괄호 깊이가 4라면 3조각
            answer += deps-1
        else:
            # 자른 막대기에서 나온 막대기
            answer += 1

print(answer)
```
