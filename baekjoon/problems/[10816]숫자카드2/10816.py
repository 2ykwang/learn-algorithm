
"""
    문제 이름: 숫자 카드 2
    문제 번호: 10816
    문제 링크: https://www.acmicpc.net/problem/10816
    난이도: Silver IV
    태그: 이분 탐색, 자료 구조, 해시를 사용한 집합과 맵, 정렬
""" 
import sys
from collections import defaultdict


def input(): return sys.stdin.readline().rstrip()


N = int(input())

cards = map(int, input().split())
dic = defaultdict(int)

for n in cards:
    dic[n] += 1

M = int(input())
nums = map(int, input().split())

for n in nums:
    print(dic[n], end=" ")
