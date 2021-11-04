---
file: "9012.py"
name: "괄호"
src: "https://www.acmicpc.net/problem/9012"
tags: 
  - 자료 구조
  - 스택
  - 문자열
done: true
draft: false
level: 7
difficulty: "Silver IV"
date: 2021-10-20
---

# 괄호

## 정답 코드

```python

# ((( )) - > depth = 1
# (( ))) - > depth = -1
# ))) ((( -> depth = 0 
n = int(input())

for i in range(n):
    ps = input()
    #현재 괄호 깊이
    depth = 0
    for chr in ps:
        # 괄호 열면 depth + 1
        if chr == '(':
            depth += 1
        # 괄호 닫으면 depth - 1
        elif chr == ')':
            depth -= 1
        # 괄호 연것보다 닫는게 많을경우 break
        if depth < 0:
            break
    # 최종적으로 괄호의 깊이가 0이 돼야 괄호 문자열이 된다.
    print("YES" if depth==0 else "NO")
```
