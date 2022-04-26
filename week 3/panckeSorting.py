class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        
        ans = []
        while arr:
            if sorted(arr) == arr:
                break
            n = len(arr) 
            for i in range(n):
                if arr[i] == n:
                    arr = arr[i::-1] + arr[i+1:]
                    ans.append(i+1)
                    arr = arr[::-1]
                    ans.append(n)
                    break
            arr.pop()
        return ans
            