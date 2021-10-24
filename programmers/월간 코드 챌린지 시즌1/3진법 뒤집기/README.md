---
file: "3진법 뒤집기.cs"
name: "3진법 뒤집기"
src: "https://programmers.co.kr/learn/courses/30/lessons/68935"
tags:
  - 월간 코드 챌린지 시즌1
done: true
date: 2021-10-23
---

# 3진법 뒤집기

## 정답 코드

```csharp
using System;

public class Solution {
    public int solution(int n) {

        // 1억 이하의 수를 3진법으로 변환한 후 자릿수가 20자리보다 클 수 없다.
        var arr = new int[20];
        // 자릿수
        int depth = 0;
        double answer = 0;

        while (n > 0)
        {
            int mod = n % 3;
            n /= 3;
            // 나머지 값을 arr 변수에 저장한다.
            arr[depth++] = mod;
        }

        for(int i=0; depth > 0; i++)
        {
            // 역순으로 계산
            int num = arr[--depth];
            if (num == 0) continue;
            answer += num*Math.Pow(3, i);
        }

        return (int)answer;
    }
}
```
