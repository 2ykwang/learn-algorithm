---
file: "1966.md"
name: "프린터 큐"
src: "https://www.acmicpc.net/problem/1966"
tags: 
  - 자료 구조
  - 구현
  - 큐
  - 시뮬레이션
done: false
draft: true
level: 8
difficulty: "Silver III"
date: 2021-10-21
---

```

def input(): return sys.stdin.readline()

def find(lst, key, find_value):
    for i, dic in enumerate(lst):
        if dic[key] == find_value:
            print(f"{dic[key]} {find_value}")
            return i+1
    return -1

n = int(input())
for _ in range(n):
    count, target = map(int, input().split())
    priority = [{"index": idx, "value": val}
                for idx, val in enumerate(input().split())] 
    print(f"{priority}")
    for i in range(len(priority)):
        for j in range(i,len(priority)):
            if priority[i]["value"]<priority[j]["value"]: 
                priority[i], priority[j]=priority[j],priority[i]

    # priority = sorted(priority, key= lambda x: (x["value"]), reverse=True)
    print(f"{priority}")
    print(find(priority, "index", target))

# seq = [1,2,3,4]
# sorted_seq = sorted(seq)

# print(seq)
# print(sorted_seq)

```