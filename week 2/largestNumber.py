class Solution:
    def largestNumber(self, nums: List[int]) -> str:
             output =''
             nums2 =[]
             for num in nums:
                new= ''.join(str(num))   
                while len(new) < 10:
                     new *= 2  
                nums2.append(new)
             for i in range(len(nums2)):
                   for j in range(i+1, len(nums2)):
                        if nums2[i][:10] <= nums2[j][:10]:
                            nums[i], nums[j] = nums[j],nums[i]
                            nums2[i], nums2[j] = nums2[j],nums2[i]
                            
             for i in nums:
                 output += str(i)
             if int(output) == 0:
                 return str(0)
             return output



nums =[12341,123411234]
print(largestNumber(nums))

     
     