class Solution:
    def tribonacci(self, n: int) -> int:
        dp = [0, 1, 1]
        
        for i in range(3, n+1):
            dp.append(dp[i-3] + dp[i-2] + dp[i-1]);
        
        return dp[n]

s = Solution()
answer = s.tribonacci(4)

print(answer)
# 4