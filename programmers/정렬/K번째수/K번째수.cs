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
            int[] destArray = new int[size];
            Array.Copy(array, s - 1, destArray, 0, size);
            Array.Sort(destArray);
            answer[i] = destArray[k - 1];
        }
        return answer;
    }
}