from functools import lru_cache
class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        def findWinner(start, end, score, turn):
            if start > end:
                return score >= 0
            if turn:
                return findWinner(start + 1, end, score + nums[start], False) or findWinner(start, end - 1, score + nums[end], False)
            else:
                return findWinner(start + 1, end, score - nums[start] , True) and findWinner(start, end - 1, score - nums[end], True)
                
            
            
            
        return findWinner(0, len(nums)-1, 0, True)
            
            
            
            

        