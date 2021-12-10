def countingValleys(steps, path):
    ctr=0
    valley = 0
    for i in range(0,steps) :
        if path[i] == "D":
            ctr -=1
        elif path[i] == "U":
            ctr +=1
        if ctr == 0 and path[i]=="U":
            valley+=1 
    print(valley)
    return valley

    