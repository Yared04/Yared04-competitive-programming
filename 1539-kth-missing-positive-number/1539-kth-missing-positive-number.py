class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        set_arr = set(arr)
        i = 1
        cnt = 0
        while True:
            if i not in set_arr:
                cnt += 1
            if cnt == k:
                return i
            i += 1