---
file: "1158.md"
name: "요세푸스 문제"
src: "https://www.acmicpc.net/problem/1158"
tags: 
  - 자료 구조
  - 큐
done: true
draft: false
level: 6
difficulty: "Silver V"
date: 2021-10-20
---

# 요세푸스 문제

## 통과한 코드

```python
n, k = [int(input_num) for input_num in input().split(' ')]

nums = [i for i in range(1, n + 1)]
answer = []

current_index = k
while len(answer) != n:
    # 남은 사람
    size = len(nums)
    # 제거 할 사람
    # nums
    target = current_index - 1 if size > current_index else ((current_index-1) % size)

    answer.append(nums.pop(target))
    current_index = target + k

# 아래 처럼 출력하면 틀리는 거 같다..
# print(answer)
# 요구하는 출력
print (f"<{', '.join(map(str, answer))}>")
```

리스트 [1, 2, 3] 이 주어지면 배열범위(0, 1, 2) 안에서 접근이 가능하다. 범위를 넘어서 접근 하려고 하면 `out of index` 에러가 발생하게 된다.

요세푸스 순열은 `삭제된 인덱스 + k` 번쨰 요소가 다음에 제거될 요소인데, 만약 그 값이 배열 크기보다 크다면 배열 크기를 나눈 나머지가 다음에 삭제될 요소가 되고 작다면 그냥 삭제하면 된다.

```python
index = 6
a = [1,2,3]

if len(a) > r:
    print(a[index])
else:
    print(a[index%len(a)])
```

제출해도 틀렸다고 나와서 코드 구현에서 문제가 있는 줄 알았는데
알고보니 출력 형식이 맞지 않아 오답처리가 됐던 거 같다. 문제에서 요구하는 출력 형식을 주의 깊게 봐야겠다.

## 시간 초과 코드

```python
# n = 전체 사람 수

que = Queue()
answer = []

for i in range(1, n+1):
    que.put(i)

# queue가 모두 비워질 때 까지 반복
while que.empty() == False:
    for i in range(k-1):
        # k-1번 만큼 pop , push 함
        tmp = que.get()
        que.put(tmp)

    # k 번 순회 후 pop된 요소
    answer.append(que.get())

print(answer)
```
