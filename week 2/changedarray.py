def  findOriginalArray(changed):
    output=[]
    if len(changed)%2 != 0:
        return output
    else:
        # changed.sort()
        for i in range(len(changed)):
            for j in range(len(changed)):
                if len(output) == len(changed)//2:
                        break 
                if changed[i]*2 == changed[j]:
                    output.append(changed[i])
                    changed.pop(i)
                    changed.pop(j)
                # elif changed[i]/2 == changed[j]:
                #     output=[]
                #     output.append(changed[j])
                               
    return output

change = [1,3,4,2,6,8]

print(findOriginalArray(change))

