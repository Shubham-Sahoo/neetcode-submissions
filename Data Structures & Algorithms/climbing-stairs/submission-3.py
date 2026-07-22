class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0 for i in range(2)]
        if n < 2:
            return 1
        dp[0] = 1
        dp[1] = 2

        for i in range(2, n):
            temp = dp[1]
            dp[1] = dp[0] + dp[1]
            dp[0] = temp
        
        return dp[1]
            

        