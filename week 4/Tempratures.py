def dailyTemperatures(temperatures):
        index = []
        arr = [0]*len(temperatures)
        index.append(0)
        for i in range(1,len(temperatures)):
            if temperatures[i]>temperatures[index[-1]]:
                while len(index)>0 and temperatures[i]>temperatures[index[-1]]:
                    k = index.pop()
                    arr[k] = i - k
                    
                index.append(i)
            else:
                index.append(i)
                
        return arr

            
        
        
arr =  [73,74,75,71,69,72,76,73]    
print(dailyTemperatures(arr))