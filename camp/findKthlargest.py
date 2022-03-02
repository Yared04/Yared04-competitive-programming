class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        for i in range(len(nums)):
            nums[i] *= -1
        heapq.heapify(nums)
        # print(nums)
        for i in range(k):
            temp = heapq.heappop(nums)
        return -temp
        