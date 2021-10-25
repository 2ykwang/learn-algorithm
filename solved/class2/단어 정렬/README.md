---
file: "1181.py"
name: "단어 정렬"
src: "https://www.acmicpc.net/problem/1181"
tags:
  - Class 2
  - 정렬
done: true
date: 2021-10-25
---

# 단어 정렬

## 정답 코드

README.md 파일을 자동으로 생성하는 파이썬 스크립트 [generator.py](../../../generator.py)를 만들었을 때 sorted 함수를 이용해서 문제해결 여부, 문제생성 시간, 문제 유형.. 등 여러가지 조건으로 정렬을 할 때 key 매개변수를 사용했었다. 그 방법이 생각나서 쉽게 풀 수 있었던 거 같다.

`단순히 중복제거 -> 문자열 길이순 정렬 -> 길이가 같다면? -> 사전순 비교`를 하는 문제여서 파이썬 내장함수만 잘 이용한다면 쉽게 풀 수 있을 거 같다.

```python
import sys

def input(): return sys.stdin.readline().rstrip()

n = int(input())

# set을 이용해 입력한 단어를 저장한다.
# set은 중복된 값을 가질 수 없다.
words = set(input() for _ in range(n))
# 단어를 정렬한다. sorted 함수 내 매개변수인 key에 lambda 를 이용해 정렬조건을 변수로 넘길 수 있다.
# 튜플을 이용해 단어길이를 기준 우선 정렬하고 문자열 비교(사전순)를 통해 정렬한다.
answer = sorted(words, key=lambda x: (len(x), x))

print('\n'.join(answer))
```

## 시간 초과 코드

왜 링크드 리스트를 써서 구현했는지 사실 구현하고나서 설명이 안됐다.. 링크드 리스트를 항상 정렬된 상태로 유지하려면 삽입할때 마다 원소개수 n개 만큼 검사를 해줘야한다 당연히 테스트케이스를 통과 못하고 시간초과가 된다.

```python
import sys

class Node(object):
    def __init__(self, value: str, prev=None, next=None):
        self.value = value
        self.prev = next
        self.next = next

class LinkedList(object):
    def __init__(self):
        self.head = Node(None)
        self.tail = Node(None)
        self.head.next = self.tail
        self.tail.prev = self.head

    def append(self, value: str):

        current_node = self.head.next
        while current_node is not self.tail:
            # 검사 로직, 길이, 같다면 사전순
            cur_value_len = len(current_node.value)
            value_len = len(value)
            if (current_node.value == value or cur_value_len > value_len or not (cur_value_len<value_len)):
                break
            current_node = current_node.next

        if current_node.value != value:
            new_node = Node(value)

            new_node.prev = current_node.prev
            new_node.next = current_node
            current_node.prev.next = new_node
            current_node.prev = new_node

    def print(self):
        current_node = self.head.next
        while current_node is not self.tail:
            print(f"{current_node.value}")
            current_node = current_node.next


def input(): return sys.stdin.readline().strip()


n = int(input())


llist = LinkedList()
for _ in range(n):
    word = input()
    llist.append(word)

llist.print()
```
