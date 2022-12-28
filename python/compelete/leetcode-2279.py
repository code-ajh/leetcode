# 2279. Maximum Bags With Full Capacity of Rocks
# test case

import heapq

capacity = [2,3,4,5]
rocks = [1,2,4,4]
additionalRocks = 2
# Output: 3

capacity = [10,2,2]
rocks = [2,2,0]
additionalRocks = 100
# Output: 3


# Solution class
class Solution:
    def maximumBags(self, capacity: list[int], rocks: list[int], additionalRocks: int) -> int:
        
        # 남은 갯수를 저장할 리스트
        rest_capacity :list[int] = []
        
        # 꽉찬 가방 카운트
        answer :int = 0
        
        # 두 리스트가 길이가 같으므로 한번만 순회
        for i in range(len(capacity)):
            
            # 가방의 용량이 꽉찬 경우 카운트
            if capacity[i] - rocks[i] <= 0:
                answer += 1
            # 가방이 꽉차지 않은 경우 힙큐에 해당 공간을 저장
            else:
                heapq.heappush(rest_capacity, capacity[i]-rocks[i])
                
        # 힙큐가 비어있는 경우 이미 모든 가방에 공간이 없음
        if len(rest_capacity) == 0:
            return len(capacity)
        
        # 추가분의 돌이 떨어지거나 모든 가방이 공간이 없을때까지 반복
        while rest_capacity and additionalRocks > 0:
            
            # 남은 공간 
            space = heapq.heappop(rest_capacity)
            
            # 남은 공간이 돌보다 클 경우 종료
            if space > additionalRocks:
                break
            
            # 돌 갯수에서 공간 만큼 빼고 가방 카운트 +1
            else:
                additionalRocks -= space
                answer += 1
        
        
        return answer
                
                


# main 
if __name__ == "__main__":
    
    a = Solution()
    
    # insert method here
    print(a.maximumBags(capacity=capacity,rocks=rocks,additionalRocks=additionalRocks))