from functools import lru_cache
class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        def findWinner(start, end, p1Score, p2Score, turn):
            if start > end:
                return p1Score >= p2Score
            if turn:
                return findWinner(start + 1, end, p1Score + nums[start], p2Score, False) or findWinner(start, end - 1, p1Score + nums[end], p2Score, False)
            else:
                return findWinner(start + 1, end, p1Score, nums[start] + p2Score, True) and findWinner(start, end - 1, p1Score, nums[end] + p2Score, True)
                
            
            
            
        return findWinner(0, len(nums)-1, 0, 0, True)
            
            
            
            

        