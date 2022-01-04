class Solution:
    def recurs(self,nums):
        if len(nums) == 1:
            return nums[0]
        else:
            return max (nums[0] - self.recurs(nums[1:]),nums[-1] - self.recurs(nums[:-1]))
        
    def PredictTheWinner(self, nums) -> bool:
        if self.recurs(nums) >= 0:
            return True
        return False
    
one = Solution()
print(one.PredictTheWinner([1,5,2]))