class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        nums.sort()
        left = 1
        right = nums[-1]
        # res = nums[-1]
        while left <= right:
            mid = (left + right)//2
            if math.ceil(nums[-1]/mid ) <= threshold:
                answer = 0
                for i in range(len(nums)):
                    answer +=  math.ceil((nums[i])/mid)
                if answer <= threshold:                 
                    res = mid
                    right = mid - 1
                else:
                    left = mid + 1
     
            elif  math.ceil(nums[-1] /mid) > threshold:
                left = mid + 1
            else:
                return res
        return res
        