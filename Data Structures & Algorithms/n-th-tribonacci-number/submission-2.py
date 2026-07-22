class Solution:
    def tribonacci(self, n: int) -> int:

        dfs = [0,1,1]
        if n<=0:
            return 0
        
        for i in range(3, n+1):
            temp = dfs[2]
            dfs[2] = dfs[0] + dfs[1] + dfs[2]  
            dfs[0] = dfs[1]
            dfs[1] = temp

        return dfs[2]

    