def kthLargestNumber(nums, k):
    numbers=[]
    for num in nums:
        numbers.append(int(num))
    print(numbers)
    numbers.sort(reverse=True)
    return str(numbers[k-1])
        
    
    
    
nums=["3","6","7","10"]
nums.sort()
# print(nums)
print(kthLargestNumber(nums,4))