# test case

n = 4

class Solution:
            

    def climbStairs(self, n: int) -> int:

        dp :list[int] = [1,2,3]
        
        for i in range(3, n):
            dp.append(dp[i-1] + dp[i-2])
        
        print(dp[n-1])


if __name__ == "__main__":
    
    a = Solution()
    
    a.climbStairs(n)