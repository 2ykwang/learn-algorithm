
"""
    문제 이름: 낚시왕
    문제 번호: 17143
    문제 링크: https://www.acmicpc.net/problem/17143
    난이도: Gold II
    태그: 구현, 시뮬레이션
"""
import sys
from typing import Tuple


def input(): return sys.stdin.readline().rstrip()

TOP = 1
DOWN = 2
RIGHT = 3
LEFT = 4
 
direction_reverse = {TOP: DOWN,
        DOWN: TOP,
        RIGHT: LEFT,
        LEFT: RIGHT}

class Shark:
    def __init__(self, x, y, s, d, z) -> None:
        self.x = x
        self.y = y
        self.speed = s
        self.direction = d
        self.size = z

    def reverse_direction(self) -> None:
        self.direction = direction_reverse[self.direction]

    def move(self, x, y) -> Tuple:
        self.x = x
        self.y = y
        return x, y

    def __check_boundry(self, width, hegiht) -> Tuple:

        if self.x > width or self.x < 0:
            self.reverse_direction()
            dis = abs(self.x-width)

            return (False, dis if self.direction == 4 else dis)

        if self.y > hegiht or self.y < 0:
            self.reverse_direction()
            dis = abs(self.x-hegiht)-1

            return (False, dis if self.direction == 2 else dis)

        return (True, 0)

    def moveVec(self, width, hegiht) -> Tuple:
        """
            @return: 새로운 좌표 (x, y)
        """
        speed = self.speed
        direction = self.direction
        cur_x, cur_y = self.x, self.y 

        if direction == 1:
            self.move(cur_x, cur_y-speed)
            c = self.__check_boundry(width, hegiht)
            if not c[0]:
                self.move(self.x, c[1])
            return self.x, self.y

        if direction == 2:
            self.move(cur_x, cur_y+speed)
            c = self.__check_boundry(width, hegiht)
            if not c[0]:
                self.move(self.x, c[1])
            return self.x, self.y

        if direction == 3:
            self.move(cur_x+speed, cur_y)
            c = self.__check_boundry(width, hegiht)
            if not c[0]:
                self.move(c[1], self.y)
            return self.x, self.y

        if direction == 4:
            self.move(cur_x-speed, cur_y)
            c = self.__check_boundry(width, hegiht)
            if not c[0]:
                self.move(c[1], self.y)
            return self.x, self.y

    def __str__(self) -> str: 
        direction_text = {TOP: "위", DOWN: "아래", RIGHT: "우측", LEFT: "좌측"}
        return f"{self.x}|{self.y}|{direction_text[self.direction]}"


class Grid:
    def __init__(self, width, height):
        self.__grid = [[None]*width for _ in range(height)]
        self.sharks: list[Shark] = []
        self.width = width
        self.height = height

    def add_shark(self, s: Shark) -> None:
        self.__grid[s.y][s.x] = s
        self.sharks.append(s)

    def move_sharks(self):

        for shark in self.sharks:
            before_x, before_y = shark.x, shark.y
            new_pos = shark.moveVec(self.width, self.height)

            self.__grid[before_y][before_x] = None
            self.__grid[new_pos[1]][new_pos[0]] = shark

    def print_grid(self):
        for y in range(self.height):
            print(f"{', '.join(map(str,self.__grid[y]))}")


g = Grid(6, 4)

g.add_shark(Shark(2, 0, 5, DOWN, 1))
g.print_grid()
g.move_sharks()
print("")
g.print_grid()  
g.move_sharks()
print("")
g.print_grid()  

# width, height, shark_count = map(int, input().split())

# make grid
