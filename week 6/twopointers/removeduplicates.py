def removeDuplicates(nums) -> int:
        i, j = 0,1
        print(len(nums))
        while i < len(nums):
            try:
                while nums[i] == nums[j]:
                    nums.pop(j)
            except:IndexError
            i += 1
            j += 1
        return len(nums)

nums = [0,0,1,1,1,2,2,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3]
print(removeDuplicates(nums),nums)