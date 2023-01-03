# 520. Detect Capital
# test case

word = "USA"
# Output: true

word = "FlaG"
# Output: false

word = "G"
# Output: True

# Solution class
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        
        
        if len(word) == 1:
            return True
        
        elif word[0].isupper():
            
            if word[1:].islower():
                return True
            elif word[1:].isupper():
                return True
            else:
                return False
        
        else:            
            if word[1:].islower():
                return True
            else:
                return False
                

# C로 풀면 아스키 코드를 사용한 방식일지도



# main 
if __name__ == "__main__":
    
    a = Solution()
    
    # insert method here
    print(a.detectCapitalUse(word=word))