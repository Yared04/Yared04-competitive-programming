class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        temp = nums[:]
        nums += [i for i in range(1, len(nums)+1)]
        XOR = 0
        for num in nums:
            XOR ^= num
            
        set_bit = 0
        i = 0
        while 1<<i <= XOR:
            if 1<<i & XOR:
                set_bit = 1<<i
            i += 1
        
        dup = 0
        missing = 0
        for num in nums:
            if set_bit & num == 0:
                dup ^= num
            else:
                missing ^= num
        if missing in temp:
            
            dup, missing = missing, dup
        
        return dup, missing
        
        
        
        # duplicate = 0
        # for i, num in enumerate(nums):
        #     if nums[abs(num) - 1] < 0:
        #         duplicate = abs(num)
        #     else:
        #         nums[abs(num) - 1] *= -1
        # print(nums)
        # for i in range(len(nums)):
        #     if nums[i] > 0:
        #         return duplicate, i + 1
  