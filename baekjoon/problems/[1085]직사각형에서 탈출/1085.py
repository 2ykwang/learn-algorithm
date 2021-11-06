
"""
    문제 이름: 직사각형에서 탈출
    문제 번호: 1085
    문제 링크: https://www.acmicpc.net/problem/1085
    난이도: Bronze III
    태그: 기하학, 수학
"""
import sys

def input(): return sys.stdin.readline().rstrip()
x, y, w, h = map(int, input().split()) 
print(min([x, y, w-x, h-y]))
