class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = 0
        pt = 0
        while pt < len(nums):
            # try:
                if nums[pt] == 0:
                    nums.pop(pt)
                    count += 1
                else:
                    pt += 1
            # except: IndexError