---
file: "1935.py"
name: "후위 표기식2"
src: "https://www.acmicpc.net/problem/1935"
tags:
  - 스택
  - 자료구조
done: true
date: 2021-10-21
---

# 후위 표기식2

## 정답 코드

```python

import sys

input = sys.stdin.readline

n = int(input())
expr = input().rstrip()
nums = [int(input().rstrip()) for i in range(n)]

st = []

for chr in expr:
    if chr.isalpha():
        # 입력받은 알파벳을 입력받은 숫자에 대응시켜준다
        # 테스트케이스로 주어지는 알파벳은 반드시 A - B - C - ... 순서가 지켜지는 거 같다.
        # 만약 A B C 순이 아닌 무작위라면 out of index 에러가 발생할 것이다
        st.append(nums[ord(chr)-ord('A')])
    else:
        # ABC+* 를 입력을 받았으면 (B+C)*A 계산이 된다. 
        b, a = st.pop(), st.pop()

        # 연산 결과를 스택에 넣고 반복한다. 결과적으로 단 한개의 요소가 남고 종료된다.
        if chr == '+':
            st.append(a+b)
        elif chr == '-':
            st.append(a-b)
        elif chr == '*':
            st.append(a*b)
        elif chr == '/':
            st.append(a/b)

print(f"{st[0]:0.2f}")
```
