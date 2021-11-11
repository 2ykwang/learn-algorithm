---
file: "17143.md"
name: "낚시왕"
src: "https://www.acmicpc.net/problem/17143"
tags: 
  - 구현
  - 시뮬레이션
done: false
draft: false
level: 14
difficulty: "Gold II"
date: 2021-11-09
---


```python

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
        path = {
            TOP: (0, -speed),
            DOWN: (0, speed),
            LEFT: (-speed, 0),
            RIGHT: (speed, 0)
        }
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
        print(i+1, target.size)
        sharks.remove(target)
    # 상어 이동 
    print("")
    print_sharks(sharks)
    move_shark(sharks) 
    shark_feeding(sharks)  
    print("") 
    print_sharks(sharks)

print(catch)
# width, height, shark_count = map(int, input().split())

# make grid

```

## 초기코드

```python

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
        path = {
            TOP: (0, -speed),
            DOWN: (0, speed),
            LEFT: (-speed, 0),
            RIGHT: (speed, 0)
        }
        dx, dy = path[self.direction]
        # print(dx, dy)
        self.__move(cur_x + dx, cur_y + dy)
        check = self.__check_boundry(width, height)

        return self.x, self.y

    def __str__(self) -> str:
        direction_text = {TOP: "위", DOWN: "아래", RIGHT: "우측", LEFT: "좌측"}
        return f"{self.x}|{self.y}|{self.speed}|{direction_text[self.direction]}|{self.size}"


class Grid:
    def __init__(self, width, height):
        self.__grid = [[None]*width for _ in range(height)]
        self.sharks: list[Shark] = []
        self.width = width
        self.height = height

    def add_shark(self, s: Shark) -> None:
        self.__grid[s.y][s.x] = s
        self.sharks.append(s)

    def remove_near_shark(self, column) -> int:
        if column >= self.width:
            return 0

        for i in range(self.height):
            target = self.__grid[i][column]
            if target is not None:
                size = target.size
                self.sharks.remove(target)
                self.__grid[i][column] = None
                return size
        return 0

    def move_sharks(self):

        for shark in self.sharks:
            before_x, before_y = shark.x, shark.y
            new_x, new_y = shark.moveVec(self.width, self.height)

            self.__grid[before_y][before_x] = None
            target: Shark = self.__grid[new_y][new_x]
            if target != None:
                # 새로 들어온 상어가 크기가 더 클 경우
                if target.size <= shark.size:
                    self.__grid[new_y][new_x] = shark
                    self.sharks.remove(target)
                else:
                    self.sharks.remove(shark)
            else:
                self.__grid[new_y][new_x] = shark

    def print_grid(self):
        for y in range(self.height):
            print(f"{', '.join(map(str,self.__grid[y]))}")


height, width, shark_count = map(int, input().split())
catch = 0

g = Grid(width, height)

# 상어 추가
for i in range(shark_count):
    r, c, s, d, z = map(int, input().split())
    g.add_shark(Shark(c-1, r-1, s, d, z))

g.print_grid()
print("")

# 낚시꾼 낚시 로직
for i in range(width):
    size = g.remove_near_shark(i)
    if size > 0:
        catch += size
        print(i)
        print(size)
    g.move_sharks()
    print("")
    g.print_grid()

print(catch)
# width, height, shark_count = map(int, input().split())

# make grid

```