from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost)<=1:
            return 0
        dp=[0]*(len(cost)+1)
        for i in range(2,len(cost)+1):
            dp[i] = min(dp[i-1]+cost[i-1], dp[i-2]+cost[i-2])
        return dp[-1]

    
if __name__ == '__main__':
    test = Solution()
    # cost = [10,15,20]
    cost = [1,100,1,1,1,100,1,1,100,1]
    print(test.minCostClimbingStairs(cost))