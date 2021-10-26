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

# 460ms