from functools import lru_cache
class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        def findWinner(start, end):
            if start == end:
                return nums[start]
            option1 = nums[start] - findWinner(start + 1, end)
            option2 = nums[end] - findWinner(start, end - 1)
            return max(option1, option2)
            
            
            
        return findWinner(0, len(nums)-1) >= 0
            
            
            
            

        