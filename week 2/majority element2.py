def majorityElement(nums):
        dic = {}
        output = []
        for i in range(len(nums)):
            if nums[i] not in dic:
                dic[nums[i]] = 1
            elif nums[i] in dic:
                dic[nums[i]] += 1
        print(dic)
        for val,count in dic.items():
            if count > len(nums)/3:
                output.append(val)
        return output      
nums = [3]
print(majorityElement(nums))