# test case
import math
n = 99


class Solution:
    def numSquares(self, n: int) -> int:
        
        # Store all perfect square <= n.
        perfectSq = []
        
        # The dp array.
        dp = [math.inf] * (n+1)
        
        for i in range(1,n+1):
            
            # calculate the square of i, dp[i_sq] to 1.
            # if i_sq is smaller than or equal to n, we store it, for the dp equation.
            i_sq = pow(i,2)
            if i_sq <= n:
                perfectSq.append(i_sq)
                dp[i_sq] = 1
            
            # dp equation
            for ps in perfectSq:
            	# i has to be smaller than the perfect square number that is used to construct i
                if i<ps: break
                
                dp[i] = min(dp[i],1+dp[i-ps])
                # it is the same as dp[i] = min(dp[i],dp[ps]+dp[i-ps]) because dp[ps]=1

        return dp[n]



if __name__ == '__main__':
    
    solution = Solution()
    
    print(solution.numSquares(n))