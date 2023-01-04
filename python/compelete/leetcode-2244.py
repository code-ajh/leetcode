# 2244. Minimum Rounds to Complete All Tasks
import time
from collections import Counter

# Solution class
class Solution:
    def minimumRounds(self, tasks: list[int]) -> int:
        
        answer :int = 0
        
        for num, num_count in Counter(tasks).items():
            
            quotient, remainder = divmod(num_count, 3)
            
            if quotient < 1: 
                if remainder == 1:
                    return -1
                else:
                    answer += 1
            elif quotient >= 1:
                if remainder >= 1:
                    answer += (1 + quotient)
                else:
                    answer += quotient
                
        return answer


# Execute
if __name__ == "__main__":
    
    i :int = 1
    
    # test case
    
    inputs :list[list[int]]= \
    [
        [2,2,3,3,2,4,4,4,4,4],
        [2,3,3],
        [5,5,5,5],
        [7,7,7,7,7,7]
    ]
    
    outputs :list[int] = \
    [
        4,
        -1,
        2,
        2
    ]
    
    
    a = Solution()
    
    # insert method here
    for  input, output in zip(inputs, outputs):        
        start = time.time()
        if a.minimumRounds(tasks=input) == output:
            print(f"Case {i} : Accepted")
        else:
            print(f"Case {i} : Wrong Answer")
        end = time.time()
        print(f"time : {(end-start) * 1000:.5f} ms")