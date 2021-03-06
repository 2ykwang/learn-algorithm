"""
문제
요세푸스 문제는 다음과 같다.

1번부터 N번까지 N명의 사람이 원을 이루면서 앉아있고, 양의 정수 K(≤ N)가 주어진다. 이제 순서대로 K번째 사람을 제거한다. 한 사람이 제거되면 남은 사람들로 이루어진 원을 따라 이 과정을 계속해 나간다. 이 과정은 N명의 사람이 모두 제거될 때까지 계속된다. 원에서 사람들이 제거되는 순서를 (N, K)-요세푸스 순열이라고 한다. 예를 들어 (7, 3)-요세푸스 순열은 <3, 6, 2, 7, 5, 1, 4>이다.

N과 K가 주어지면 (N, K)-요세푸스 순열을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 N과 K가 빈 칸을 사이에 두고 순서대로 주어진다. (1 ≤ K ≤ N ≤ 5,000)
"""
n, k = [int(input_num) for input_num in input().split(' ')]

nums = [i for i in range(1, n + 1)]
answer = []

current_index = k
while len(answer) != n:
    # 남은 사람
    size = len(nums)
    # 제거 할 사람  
    # k-1 -> index 는 0부터 시작하므로
    # 제거할 index 값이 배열의 size 보다 클 경우 size를 나눈값이 인덱스가된다
    target = current_index - 1 if size > current_index else ((current_index-1) % size)
    
    # 답변에
    answer.append(nums.pop(target))
    # 다음에 제거될 사람 index
    current_index = target + k

# 아래 처럼 출력하면 틀리는 거 같다..
# print(answer)
# 요구하는 출력
print (f"<{', '.join(map(str, answer))}>")

# k-1
# 3,6,2,7,5,1,4
