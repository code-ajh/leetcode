# 1962. Remove Stones to Minimize the Total

# 

# test case

# piles = [5,4,9]
# k = 2
# Output: 12

piles = [16,3,6,7]
k = 5
# Output: 12

# piles = [2,3]
# k = 3

piles = [4122,9928,3477,9942]
k = 6
# Output: 8768

import math

# Solution class
class Solution:
    def minStoneSum(self, piles: list[int], k: int) -> int:
        
        piles.sort(reverse=True)
        idx = 0
        
        while k > 0:
                        
            if len(piles) == 1:
                piles[idx] = piles[idx] - math.floor(piles[idx]/2)
                k -=1
                
                continue
            
            if idx - 1 >= 0: 
                before_value = piles[idx-1]         
                before_idx = idx - 1
            if idx + 1 < len(piles):
                next_value = piles[idx + 1]
                next_idx = idx + 1
                
                if before_value < next_value:
                    compare_idx = next_idx
                else:
                    compare_idx = before_idx
                
                
                if piles[idx] > piles[compare_idx]:
                    continue
                else:
                    idx = compare_idx
                    
                
            else:
                piles[idx] = piles[idx] - math.floor(piles[idx]/2)
                k -=1
        
        return sum(piles)
        





# main 
if __name__ == "__main__":
    
    a = Solution()
    
    # insert method here
    print(a.minStoneSum(piles=piles,k=k))