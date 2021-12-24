def equalStacks(h1, h2, h3):
    balanced = False
    height1 =0
    height2 =0
    height3 =0
    h1.reverse()
    h2.reverse()
    h3.reverse()
    for i in range(len(h1)): 
        height1 += h1[i]
    for i in range(len(h2)):
        height2 += h2[i]
    for i in range(len(h3)):
        height3 += h3[i]
    while not balanced:
        if height1 == height3 == height2:
            balanced = True 
            return height2
        elif height1 > height2 or height1 > height3:
            height1 -= h1.pop(-1)
        elif height2 > height1 or height2 > height3:
            height2 -= h2.pop(-1)
        elif height3 > height2 or height3 > height1:
            height3 -= h3.pop(-1)
        else:
            balanced = True
            return 0
            
            

    
        
    
    
h1 = [3, 2, 1,1,1]
h2 = [4, 3]
h3 = [1, 1, 4, 1]
print(equalStacks(h1,h2,h3))