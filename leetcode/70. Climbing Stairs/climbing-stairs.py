class Solution:
    # n 값에 따른 경우의 수
    # n = 1 -> 1개
    # n = 2 -> 2개
    # n = 3 -> 3개
    # n = 4 -> 5개
    # ...
    # f(n) = f(n-1)+f(n-2)
    def climbStairs(self, n: int) -> int:
        dp = [0, 1, 2]

        for i in range(3,n+1):
            dp.append(dp[i-1]+dp[i-2])
        return dp[n]