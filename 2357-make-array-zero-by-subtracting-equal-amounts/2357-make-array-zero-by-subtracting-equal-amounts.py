class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        min_heap = []
        for num in nums:
            if num != 0:
                heappush(min_heap, num)
        cnt = 0
        while sum(nums) != 0:
            smallest = heappop(min_heap)
            min_heap = []
            for i in range(len(nums)):
                if nums[i] != 0:
                    nums[i] = nums[i] - smallest
                    if nums[i] != 0:
                        heappush(min_heap, nums[i])
            
            cnt += 1
        return cnt
                
        