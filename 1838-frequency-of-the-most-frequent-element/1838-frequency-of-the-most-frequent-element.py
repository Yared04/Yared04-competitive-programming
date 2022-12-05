class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        left,right = 0,0
        res,total = 0,0
        for right in range(len(nums)):
            total += nums[right]
            # the total sum I have got < the sum of the numbers until nums[right]
            while total + k < (right-left+1) * nums[right]:
                total -= nums[left]
                left += 1
            res = max(res,right-left+1)
        return res

            