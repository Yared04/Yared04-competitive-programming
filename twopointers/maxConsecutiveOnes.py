class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        pt1 = 0 
        pt2 = 0
        res = 0
        dif = 0
        while pt2 < len(nums) or pt1 < len(nums):
            while pt2 < len(nums) and (nums[pt2] == 1 or k):
                if nums[pt2] == 1:
                    pt2+= 1
                    # dif = pt2 - pt1
                elif nums[pt2] == 0:
                    pt2 += 1
                    k -= 1
                    
            dif = pt2 - pt1
            res = max(res, dif) 
            if pt1 < len(nums) and nums[pt1] == 0:
                k += 1
            pt1 += 1 
        return res
        