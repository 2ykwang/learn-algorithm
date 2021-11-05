---
file: "20437.md"
name: "문자열 게임 2"
src: "https://www.acmicpc.net/problem/20437"
tags:
  - 슬라이딩 윈도우
  - 문자열
done: true
draft: false
level: 11
difficulty: "Gold V"
date: 2021-11-06
---

# 문자열 게임 2

```python
import sys
from collections import defaultdict


def input(): return sys.stdin.readline().rstrip()


for _ in range(int(input())):
    chars = defaultdict(list)
    alphabet_count = [-1]*26

    text = input()
    K = int(input())

    # 전처리
    for idx, c in enumerate(text):
        m = ord(c)-ord('a')
        if alphabet_count[m] < 0:
            alphabet_count[m] = text.count(c)
        count = alphabet_count[m]

        if K <= count:
            chars[c].append(idx)
    # -
    _min, _max = 10000, 0
    for x in chars.values():
        for i in range(len(x)-K+1):
            # 0+k-1 2,
            current_length = x[i+K-1] - x[i] + 1
            _min = min(_min, current_length)
            _max = max(_max, current_length)

    if len(chars) > 0:
        print(_min, _max)
    else:
        print("-1")

```
