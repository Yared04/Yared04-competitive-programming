def checkArithmeticSubarrays(nums,l,r):
    output=[]
    for i in range(len(l)):
        new = nums[l[i]:r[i]+1]
        new.sort()
        dif = new[1]-new[0]
        print(new)
        
        for j in range(len(new)-1):
            flag = True
            if new[j+1] - new[j] != dif:
                 flag = False
                 break
        if flag == True:
            output.append(True)
        else:
            output.append(False)
                       
    return output
nums =  [-3,-6,-8,-4,-2,-8,-6,0,0,0,0]
l =  [5,4,3,2,4,7,6,1,7] 
r = [6,5,6,3,7,10,7,4,10]
print(checkArithmeticSubarrays(nums,l,r))
# print(eval("4"-"2"))
            