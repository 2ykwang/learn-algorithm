---
file: "H-Index.py"
name: "H-Index"
src: "https://programmers.co.kr/learn/courses/30/lessons/42747?language=python3#"
tags:
  - 정렬
done: true
date: 2021-10-26
---

# H-Index

## 정답 코드

```python
def solution(citations):
    # citations를 역순으로 정렬한다
    # ex) [3, 0, 6, 1, 5] - > [6, 5, 3, 0, 1]
    citations.sort(reverse=True)

    # 반환할 h-index 값
    answer = 0

    for c in citations:
        # answer 값을 후위 증감한다.
        # answer 값과 논문의 인용 횟수값을 비교해서 answer이 크거나 같으면
        # loop를 종료한다 종료 시점에 answer 값이 h-index가 된다.
        # ex) [6, 5, <3>, 0, 1]
        if answer >= c:
            break
        answer+=1
    return answer
```
