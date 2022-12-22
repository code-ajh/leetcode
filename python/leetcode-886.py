# 886. Possible Bipartition

# test case

n = 4
dislikes = [[1,2],[1,3],[2,4]]

# n = 3
# dislikes = [[1,2],[1,3],[2,3]]

n = 5
dislikes = [[1,2],[2,3],[3,4],[4,5],[1,5]]

n = 10
dislikes = [[1,2],[3,4],[5,6],[6,7],[8,9],[7,8]]

# Solution class
class Solution:
    def changeStatus(self, std: list[int], other :list[int], hate_list :list[int]):
        
        for num in hate_list:
            
            num -= 1
            
            if other[num]:
                continue
            else:
                if std[num]:
                    return False
                else:
                    other[num] = True
            
        return True
    
    def possibleBipartition(self, n: int, dislikes: list[list[int]]) -> bool:
        
        dislike_dict = dict()
        
        for num in dislikes:
            
            lower_num = num[0]
            upper_num = num[1]
                        
            dislike_dict[lower_num] = dislike_dict.get(lower_num, []) + [upper_num]


        a :list[bool] = [False] * n
        b :list[bool] = [False] * n
        
            
        for k, v in dislike_dict.items():
            
            k = k-1
            
            if a[k] and not b[k]:
                
                if self.changeStatus(std=a, other=b, hate_list=v):
                    return False
                
            elif not a[k] and b[k]:
                
                if not self.changeStatus(std=b, other=a, hate_list=v):
                    return False
            
            else:                
                if self.changeStatus(std=a, other=b, hate_list=v):
                    continue
                else:
                    if not self.changeStatus(std=b, other=a, hate_list=v):
                        return False
                    
                
                
        return True



# main 
if __name__ == "__main__":
    
    a = Solution()
    
    # insert method here
    print(a.possibleBipartition(n=n,dislikes=dislikes))