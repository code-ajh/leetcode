class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        for idx, num in enumerate(nums):
            
            value = target - num
            
            try:
                answer_idx = nums.index(value)
                if answer_idx == idx:
                    continue
                else:
                    break
            except:
                continue

        return [idx, answer_idx]
        