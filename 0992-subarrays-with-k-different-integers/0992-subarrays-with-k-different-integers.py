class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        dic = {}
        size_nums = len(nums)
        ptr = left = count = acc = 0 
        
        for right in range(size_nums):
            if nums[right] not in dic:
                dic[nums[right]] = 1
                count += 1
            else:
                dic[nums[right]] += 1
            if count > k:
                dic.pop(nums[left])
                left += 1
                count -= 1
                acc = 0
            while dic[nums[left]] > 1:
                acc += 1
                dic[nums[left]] -= 1
                left += 1
                
            if count == k:
                ptr += acc + 1
       
        return ptr  