## Title
# 452. Minimum Number of Arrows to Burst Balloons

# Import Packages
import time

# Solution class
class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        
        if len(points) == 1:
            return 1
        
        points.sort(key=lambda x:(x[1]))
        
        arrow_pos = float('-inf')
        arrow_count = 0

        for balloon in points:
            if balloon[0] > arrow_pos:
                # 풍선을 터트리기 위해 새로운 화살이 필요함
                arrow_count += 1
                arrow_pos = balloon[1]
            else:
                # 기존 화살을 사용할 수 있음
                arrow_pos = min(arrow_pos, balloon[1])

        return arrow_count
        
    


# Execute
if __name__ == "__main__":
    
    i :int = 1
    
    # test case
    
    inputs = \
    [
        [[10,16],[2,8],[1,6],[7,12]],
        [[1,2],[3,4],[5,6],[7,8]],
        [[1,2],[2,3],[3,4],[4,5]],
        [[1,3],[1,15]]      
    ]
    
    outputs = \
    [
        2,
        4,
        2,
        0
    ]
    
    
    a = Solution()
    
    # insert method here
    for  input, output in zip(inputs, outputs):        
        start = time.time()
        if a.findMinArrowShots(input) == output:
            print(f"Case {i} : Accepted")
        else:
            print(f"Case {i} : Wrong Answer")
        end = time.time()
        print(f"time : {(end-start) * 1000:.5f} ms")