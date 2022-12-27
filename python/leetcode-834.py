# 834. Sum of Distances in Tree
# test case

n = 6
edges = [[0,1],[0,2],[2,3],[2,4],[2,5]]
# Output: [8,12,6,10,10,10]

n = 1
edges = []
# Output: [0]

n = 2
edges = [[1,0]]
# Output: [1,1]

# Solution class
class Solution:
    def sumOfDistancesInTree(self, n: int, edges: list[list[int]]) -> list[int]:
        
        tree :list[int] = [x for edge in edges]
        


# main 
if __name__ == "__main__":
    
    a = Solution()
    
    # insert method here
    print(a.sumOfDistancesInTree(n=n, edges=edges))