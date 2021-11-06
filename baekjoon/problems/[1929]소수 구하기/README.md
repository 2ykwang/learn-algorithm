---
file: "1929.md"
name: "소수 구하기"
src: "https://www.acmicpc.net/problem/1929"
tags:
  - 수학
  - 정수론
  - 소수 판정
  - 에라토스테네스의 체
done: true
draft: false
level: 9
difficulty: "Silver II"
date: 2021-11-07
---

# 소수 구하기

```python
import sys

def input(): return sys.stdin.readline().rstrip()

def is_prime(m: int, n: int) -> bool:
    # n 1 이하일 경우 빈 리스트 반환
    if n <= 1:
        return []

    # n-m+1 크기를 갖는 배열 생성
    # n=10000, m= 100010 - > l = 11
    l = n-m+1
    prime = [True] * l

    # n의 제곱근 까지 loop
    # n의 약수는 반드시 sqrt(n) 범위 안에 존재한다.
    for i in range(2, int(n**0.5)+1):
        for j in range(2*i, n+1, i):
            # j-m+1 이 0보다 클때 검사한다.
            # 예를들어 m 값이 100 일경우
            # j가 100이 될때 검사하고 생성된 prime 배열 인덱스에 m 값을 빼서 매칭해준다
            if j-m >= 0 and prime[j-m]:
                prime[j-m] = False

    # m이 2미만일경우 2-m -> n-m+1 까지 루프 (0과 1 생략)
    return [x+m for x in range(2-m if m <= 2 else 0, l) if prime[x]]

nums = is_prime(*map(int, input().split()))
for n in nums:
    print(n)

# 948ms
```
