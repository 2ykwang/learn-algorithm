import sys
import heapq

def input(): return sys.stdin.readline().rstrip()

n = int(input())
q = []

for _ in range(n):
    for num in list(map(int,input().split())):  
        if len(q) < n:
            heapq.heappush(q, num)
        elif q[0] < num:
            heapq.heappush(q, num)
            heapq.heappop(q)
        
print(heapq.heappop(q))

# PriorityQueue - > 1988ms
# heapq -> 1140ms