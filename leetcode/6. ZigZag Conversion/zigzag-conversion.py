"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:


"""

class Solution:
    def convert(self, s: str, numRows: int) -> str:

        if numRows == 1:
            return s
        
        rows = [[] for _ in range(numRows)]
        down = True
        seq = 0

        for chr in s:
            rows[seq].append(chr)
            seq += 1 if down else -1
            if seq == 0 or seq == numRows-1:
                # flip
                down = not down

        return ''.join([''.join(r) for r in rows])


s = Solution()
result = s.convert("AB",1)
print(result)