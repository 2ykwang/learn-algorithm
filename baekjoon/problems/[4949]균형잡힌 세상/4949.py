
"""
    문제 이름: 균형잡힌 세상
    문제 번호: 4949
    문제 링크: https://www.acmicpc.net/problem/4949
    난이도: Silver IV
    태그: 자료 구조, 스택, 문자열
"""
import sys


def input(): return sys.stdin.readline().rstrip()


parentheses = {
    ')': '(',
    ']': '[',
}
open_parentheses = parentheses.values()
close_parentheses = parentheses.keys()


def solve(text: str) -> bool:
    st = []
    for c in text:
        if c in open_parentheses:
            st.append(c)

        elif c in close_parentheses:
            if len(st) > 0 and st[-1] == parentheses[c]:
                st.pop()
            else:
                return False

    return len(st) == 0


while True:
    text = input()

    if text == '.':
        break

    print("yes" if solve(text) else "no")

# 108ms
