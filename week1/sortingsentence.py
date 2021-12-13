def sortSentence(s):
     newList = s.split()
 
     for i in range(len(newList)):
        for j in range(i+1, len(newList)):
            if int(newList[i][-1]) > int(newList[j][-1]):
                newList[i],newList[j] = newList[j],newList[i]
     for i in range(len(newList)):
          newList[i]= newList[i][:-1]       
     sentence = " ".join(newList)
     return sentence
s = "Myself2 Me1 I4 and3"
print(sortSentence(s))
