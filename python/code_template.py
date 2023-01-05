## Title

# Import Packages
import time

# Solution class
class Solution:
    pass


# Execute
if __name__ == "__main__":
    
    i :int = 1
    
    # test case
    
    inputs = \
    [
    ]
    
    outputs = \
    [
    ]
    
    
    a = Solution()
    
    # insert method here
    for  input, output in zip(inputs, outputs):        
        start = time.time()
        if a.method(input) == output:
            print(f"Case {i} : Accepted")
        else:
            print(f"Case {i} : Wrong Answer")
        end = time.time()
        print(f"time : {(end-start) * 1000:.5f} ms")