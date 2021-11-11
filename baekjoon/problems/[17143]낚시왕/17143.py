
"""
    문제 이름: 낚시왕
    문제 번호: 17143
    문제 링크: https://www.acmicpc.net/problem/17143
    난이도: Gold II
    태그: 구현, 시뮬레이션
"""

import sys
from typing import List, Tuple


def input(): return sys.stdin.readline().rstrip()


TOP = 1
DOWN = 2
RIGHT = 3
LEFT = 4

direction_reverse = [None, DOWN, TOP, LEFT, RIGHT]  # 위치 반전


class Shark:
    def __init__(self, x, y, s, d, z) -> None:
        self.x = x
        self.y = y
        self.speed = s
        self.direction = d
        self.size = z

    def reverse_direction(self) -> None:
        self.direction = direction_reverse[self.direction]

    def __move(self, x, y) -> Tuple:
        self.x = x
        self.y = y
        return x, y

    def __check_boundry(self, width, height) -> Tuple[bool, int, int]:

        if self.x >= width or self.x < 0:
            self.reverse_direction()
            boundry = width-1
            dis = abs(boundry-self.x) if self.x >= width else self.x

            self.__move(boundry-dis if self.direction == LEFT else dis, self.y)

            if self.x >= width or self.x < 0:
                return self.__check_boundry(width, height)

            return (False, boundry-dis if self.direction == LEFT else dis, self.y)

        if self.y >= height or self.y < 0:
            self.reverse_direction()
            boundry = height-1
            dis = abs(boundry-self.y) if self.y >= height else self.y

            self.__move(self.x, boundry-dis if self.direction == TOP else dis)

            if self.y >= height or self.y < 0:
                return self.__check_boundry(width, height)

            return (False, self.x, boundry-dis if self.direction == TOP else dis)

    def moveVec(self, width, height) -> Tuple[int, int]:
        """
            @return: 새로운 좌표 (x, y)
        """
        speed = self.speed
        direction = self.direction
        cur_x, cur_y = self.x, self.y
        path = [None,
                (0, -speed),
                (0, speed),
                (-speed, 0),
                (speed, 0),
                ]

        dx, dy = path[self.direction]
        # print(dx, dy)
        self.__move(cur_x + dx, cur_y + dy)
        check = self.__check_boundry(width, height)

        return self.x, self.y

    def __str__(self) -> str:
        direction_text = {TOP: "위", DOWN: "아래", RIGHT: "우측", LEFT: "좌측"}
        return f"{self.x}|{self.y}|{self.speed}|{direction_text[self.direction]}|{self.size}"


height, width, shark_count = map(int, input().split())
catch = 0

sharks: List[Shark] = []
grid = [[None]*width for _ in range(height)]


def move_shark(sharks: List[Shark]) -> None:
    for shark in sharks:
        shark.moveVec(width, height)


def shark_feeding(sharks: List[Shark]) -> None:
    for i in range(len(sharks)):
        for j in range(len(sharks)):
            if i < len(sharks) and j < len(sharks) and i != j and sharks[i].x == sharks[j].x and sharks[i].y == sharks[j].y:
                if sharks[i].size > sharks[j].size:
                    sharks.remove(sharks[j])
                elif sharks[i].size < sharks[j].size:
                    sharks.remove(sharks[i])


def print_sharks(sharks: List[Shark]) -> None:
    grid = [[None]*width for _ in range(height)]
    for shark in sharks:
        grid[shark.y][shark.x] = shark

    for y in range(height):
        print(f"{', '.join(map(str,grid[y]))}")


# 상어 추가
for i in range(shark_count):
    r, c, s, d, z = map(int, input().split())
    sharks.append(Shark(c-1, r-1, s, d, z))


# 낚시꾼 낚시 로직
for i in range(width):
    target = None
    for j in range(len(sharks)):
        # 낚시꾼이 낚는 상어
        if sharks[j].x == i and (target == None or sharks[j].y < target.y):
            target = sharks[j]
    if target != None:
        catch += target.size
        # print(i+1, target.size)
        sharks.remove(target)
    # 상어 이동
    # print_sharks(sharks)
    move_shark(sharks)
    shark_feeding(sharks)
    # print_sharks(sharks)

print(catch)
