---
file: "K번째수.py"
name: "K번째수"
src: "https://programmers.co.kr/learn/courses/30/lessons/42748?language=csharp"
tags:
  - 정렬
done: true
date: 2021-10-23
---

# K번째수

## 정답 코드

```csharp
using System;

public class Solution
{
    public int[] solution(int[] array, int[,] commands)
    {
        int[] answer = new int[commands.GetLength(0)];
        for (int i = 0; i < commands.GetLength(0); i++)
        {
            int s = commands[i, 0];
            int l = commands[i, 1];
            int k = commands[i, 2];
             
            int size = l - s + 1;
            //  l - s + 1 크기의 배열을 생성한다
            int[] destArray = new int[size];
            // 전달 받은 배열에서 지정한 길이만큼 값 복사 수행
            Array.Copy(array, s - 1, destArray, 0, size);
            // 정렬
            Array.Sort(destArray);
            // 복사한 배열에서 k-1 번째 인덱스 반환 
            answer[i] = destArray[k - 1];
        }
        return answer;
    }
}
```
