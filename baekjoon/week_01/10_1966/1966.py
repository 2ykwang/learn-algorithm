from collections import deque
import sys


def input(): return sys.stdin.readline()
queue = deque()

n = int(input())
for _ in range(n):
    count, target = map(int, input().split())
    priority = deque([{"index": idx, "value": val}
                for idx, val in enumerate(input().split())])
    print(f"{priority}") 
    for i in range(len(priority)-1):  
        if priority[i]["value"] < priority[i+1]["value"]: 
            for _ in range(i+1):
                p = priority.popleft()
                priority.append(p)
            i=0

    # priority = sorted(priority, key= lambda x: (x["value"]), reverse=True)
    print(f"{priority}")

# seq = [1,2,3,4]
# sorted_seq = sorted(seq)

# print(seq)
# print(sorted_seq)
