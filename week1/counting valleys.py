def countingValleys(steps, path):
    ctr=0
    valley = []
    for i in range(1,steps) :
        if path[i] == "D":
            ctr -=1
        elif path[i] == "U":
            ctr +=1
        if ctr == 0 and path[i-1] 
            
            valley +=1
    return valley
print(countingValleys(8,
"UDDDUDUU"))
    