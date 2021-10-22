---
file: "zigzag-conversion.py"
name: "6. ZigZag Conversion"
src: "https://leetcode.com/problems/zigzag-conversion/"
tags:
  - String
done: true
date: 2021-10-21
---
# ZigZag Conversion

## 문제

```text
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:
```

## 정답 코드

```python
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # numRows 1 이면 입력받은 문자열 그대로 반환해준다.
        if numRows == 1:
            return s
        
        # numRows 만큼 list 를 할당한다.
        rows = [[] for _ in range(numRows)]
        # 진행 방향을 나타내는 스위치 변수
        down = True
        # 현재 쓰고 있는 열 index
        seq = 0

        for chr in s:
            rows[seq].append(chr)
            # seq down True - > +1 down False - > -1 
            seq += 1 if down else -1
            if seq == 0 or seq == numRows-1:
                # flip
                down = not down

        # 2차원 배열을 공백없는 문자열로 만들어준다
        return ''.join([''.join(r) for r in rows])
```

## 문제 이해를 잘못하고 푼 코드

문제를 정확히 안읽고 문자열을 입력 받으면 아래와 같이 렌더링 되는 함수를 만들라는 건 줄 알았다.. 근데 어쨌든 통과되긴 했다 아래와 같은 풀이로 풀게 되면 공간 복잡도는 n/2*n이 된다

```text
P   A   H   N
A P L S I I G
Y   I   R
```

```python

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        space = [[' ' for _ in range((len(s)//2) +1)] for _ in range(numRows)]

        down = True
        x = 0
        y = 0
        max_x = 0
        for chr in s:
            if not down:
                space[y][x] = chr
                y-=1
                x+=1
            else:
                space[y][x] = chr
                y+=1
            max_x = max(max_x,x)
            if y>=numRows:
                y=numRows-2
                x+=1
                down=False
            if y<=0:
                down=True
        render = []
        for line in space:
            render.append(''.join(line))

        return ''.join(render).replace(" ","")
```
