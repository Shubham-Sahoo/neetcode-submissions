class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        dfs = [0 for i in range(len(cost))]
        dfs[0] = cost[0]
        dfs[1] = cost[1]

        for i in range(2, len(cost)):
            dfs[i] = min(cost[i] + dfs[i-1], cost[i] + dfs[i-2])

        print(dfs)

        return min(dfs[-2], dfs[-1])