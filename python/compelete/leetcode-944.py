# 944. Delete Columns to Make Sorted
# test case

# strs = ["cba","daf","ghi"]
# Output: 1

# strs = ["a","b"]
# Output: 0

strs = ["zyx","wvu","tsr"]
# Output: 3

strs = ["rrjk","furt","guzm"]
# Output : 2

# Solution class
class Solution:
    def minDeletionSize(self, strs: list[str]) -> int:
        
        if len(strs) == 1:
            return 0
        
        before_char :str = strs[0]
        sort_check :list[bool] = [True] * len(strs[0])
        
        answer = 0
        
        for word in strs[1:]:
            
            for idx, flag in enumerate(sort_check):                
                
                # ord() 사용해야하는 줄 알았는데 없어도 비교가 된다.
                # 예전에 써봤던 기억이 왜 이제야 날까..
                if flag and before_char[idx] <= word[idx]:
                    continue
                elif flag and before_char[idx] > word[idx]:
                    sort_check[idx] = False
                    answer += 1
                else:
                    continue
                    
            before_char = word
            
        return answer
        

# main 
if __name__ == "__main__":
    
    a = Solution()
    
    # insert method here
    print(a.minDeletionSize(strs=strs))