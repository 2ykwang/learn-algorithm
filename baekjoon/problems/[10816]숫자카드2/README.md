---
file: "10816.md"
name: "숫자 카드 2"
src: "https://www.acmicpc.net/problem/10816"
tags:
  - 이분 탐색
  - 자료 구조
  - 해시를 사용한 집합과 맵
  - 정렬
done: true
draft: false
level: 7
difficulty: "Silver IV"
date: 2021-11-12
---

# 숫자 카드 2

## 풀이 코드

```python
import sys
from collections import defaultdict


def input(): return sys.stdin.readline().rstrip()


N = int(input())

cards = map(int, input().split())
dic = defaultdict(int)

for n in cards:
    dic[n] += 1

M = int(input())
nums = map(int, input().split())

for n in nums:
    print(dic[n], end=" ")
```
