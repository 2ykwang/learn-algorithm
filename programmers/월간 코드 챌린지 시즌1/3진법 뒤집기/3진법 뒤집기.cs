using System;

public class Solution {
    public int solution(int n) { 
        
        var arr = new int[20];
        int depth = 0;
        double answer = 0;
        
        while (n > 0)
        {
            int mod = n % 3;
            n /= 3;
            arr[depth++] = mod;
        }

        for(int i=0; depth > 0; i++)
        { 
            int num = arr[--depth]; 
            if (num == 0) continue;
            answer += num*Math.Pow(3, i);
        } 
        
        return (int)answer;
    }
}