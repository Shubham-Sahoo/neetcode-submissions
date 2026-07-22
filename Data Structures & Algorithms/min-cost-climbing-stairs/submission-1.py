class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        dfs = [0 for i in range(2)]
        dfs[0] = cost[0]
        dfs[1] = cost[1]

        for i in range(2, len(cost)):
            temp = dfs[1]
            dfs[1] = min(cost[i] + dfs[1], cost[i] + dfs[0])
            dfs[0] = temp

        print(dfs)

        return min(dfs[-2], dfs[-1])