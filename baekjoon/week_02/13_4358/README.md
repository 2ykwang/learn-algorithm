---
file: "4358.py"
name: "생태학"
src: "https://www.acmicpc.net/problem/4358"
tags:
  - 자료 구조
  - 문자열
  - 트리를 사용한 집합과 맵
  - 해시를 사용한 집합과 맵
done: true
date: 2021-10-26
---

# 생태학

## 정답 코드

나무 이름이 언급된 횟수를 카운트하고 이름 순서대로 사전순 정렬 후 출력하면 되는 문제다.

```python
from collections import defaultdict
import sys

test_data = sys.stdin.read().split('\n')[:-1]

# dictionary 키에 접근할 때 None 체크를 안하고 바로 사용 할 수 있다.
# 타입을 명시해야하며 count 해야하니 타입은 int
dic = defaultdict(int)

for word in test_data:
    dic[word] += 1

# 언급된 나무 이름 기준으로 데이터를 내림차순 정렬한다.
sorted_dic = sorted(dic.items(), key=lambda x: x[0])

# 전체 나무 이름
tree_count = len(test_data)

for item in sorted_dic:
    print(f"{item[0]} {(item[1]/tree_count)*100:.4f}")

# 445ms
```

## 처음에 놓친 부분

맨 처음에 구현한 입력을 받는 코드다. 공백 문자열이 올 때 까지 입력을 받는다. 속도가 느리다.

### 느린 입력 코드

```python
while True:
    input_word = sys.stdin.readline().rstrip()
    if len(input_word) < 1:
        break
    test_data.append(input_word)
```

### 좀 더 빠른 입력 코드

아래와 같이 간단하게 쓸 수 있다. 실제로 채점결과에서 속도도 2배이상 차이가 났다.

```python
test_data = sys.stdin.read().split('\n')[:-1]
```
