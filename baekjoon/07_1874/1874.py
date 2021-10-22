import sys

def input(): return sys.stdin.readline().rstrip()

n = int(input())
nums = [int(input()) for i in range(n)]

st = []
answer = []
cur = 0
for num in nums:
    # cur이 num과 같을 때 까지 push
    while cur < num:
        cur += 1
        st.append(cur)
        answer.append("+")
    # 스택 마지막요소가 num 일경우 pop
    if st[-1] == num:
        st.pop()
        answer.append("-")
        continue
    else:
        # 스택 마지막요소가 num이 아닐경우 만들어질 수 없는 수열
        # ex [1 2 3] 인데 숫자 4가 올경우
        print("NO")
        break

# 수를 모두 사용하여 스택이 비워져 있을 경우에만 출력해준다.
if len(st) == 0:
    print('\n'.join(answer)) 