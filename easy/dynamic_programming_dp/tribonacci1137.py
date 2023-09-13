class Solution:
    def tribonacci(self, n: int) -> int:
        if n==0:
            return 0
        if n<=2:
            return 1
        # base case
        dp = [0]*(n+1)
        dp[0] = 0
        dp[1] = 1
        dp[2] = 1
        for i in range(3, n+1):
            dp[i] = dp[i-3] + dp[i-2] + dp[i-1]
        return dp[n]

if __name__ == '__main__':
    test = Solution()
    # n = 4
    n = 25
    print(test.tribonacci(n))
