class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        two_powers = ['1']
        i = 1
        while len(two_powers[-1]) < 10:
            two_powers.append(str(2**i))
            i += 1
        
        

        def checkPresence(it1, it2):
            temp = Counter(it1)
            list_it2 = list(it2)
            # print(it1, temp, it2, list_it2)
            while list_it2:
                cur_num = list_it2.pop()
                if temp.get(cur_num, 0) < 1:
                    return False
                temp[cur_num] -= 1
            return True
               
            
        str_n = str(n)
        for pw2 in two_powers:
            if len(pw2) == len(str_n):
                if checkPresence(pw2, str_n):
                    # print(pw2, str_n)
                    return True
        return False
                
            
        