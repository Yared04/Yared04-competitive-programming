class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        count = Counter(nums)
        for val in count.values():
            if val != 1:
                return True
        return False