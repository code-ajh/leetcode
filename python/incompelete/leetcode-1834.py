# 1834. Single-Threaded CPU
# test case

tasks = [[1,2],[2,4],[3,2],[4,1]]
# Output: [0,2,3,1]

# tasks = [[7,10],[7,12],[7,5],[7,4],[7,2]]
# Output: [4,3,2,0,1]

# Solution class
class Solution:
    def getOrder(self, tasks: list[list[int]]) -> list[int]:
        
        tasks = [x + [idx] for idx, x in enumerate(tasks)]
        
        print(tasks)
        
    

# main 
if __name__ == "__main__":
    
    a = Solution()
    
    # insert method here
    print(a.getOrder(tasks=tasks))