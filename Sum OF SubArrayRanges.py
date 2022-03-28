class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        pt1 = 0
        ans = 0
        while pt1 < len(nums):
            pt2 = pt1
            maxx = nums[pt1]
            minn = nums[pt2] 
            while pt2 < len(nums):
                ans += maxx - minn
                pt2 += 1
                if pt2 == len(nums):
                    break
                maxx = nums[pt2] if nums[pt2] > maxx else maxx
                minn = nums[pt2] if nums[pt2] < minn else minn
                
            pt1 += 1
        
        return ans
                
        
        
