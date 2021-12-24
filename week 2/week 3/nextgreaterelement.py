def nextGreaterElement( nums1, nums2):
        rem = {}
        stac = []
        for i in range(len(nums2)):
            for j in range(i, len(nums2)):
                if nums2[i] < nums2[j]:
                    rem[nums2[i]]  = nums2[j]
                    break
                else: 
                    rem[nums2[i]] = -1  
        for j in range(len(nums1)):
            stac.append(rem[nums1[j]])
            
        return stac
        
nums1 = [2,4]
nums2 = [1,2,3,4]
print(nextGreaterElement(nums1,nums2))