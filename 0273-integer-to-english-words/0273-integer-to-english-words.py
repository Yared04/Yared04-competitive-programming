class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0: 
            return "Zero"
        mapper = {
            1: ["One"], 2: ["Two","Twenty"], 3: ["Three","Thirty" ], 4: ["Four", "Forty"], 5: ["Five", "Fifty"], 6: ["Six", "Sixty"], 7: ["Seven", "Seventy"], 8: ["Eight", "Eighty"], 9: ["Nine", "Ninety"]
        }
        
        specialMapper = { 10: "Ten", 11: "Eleven", 12: "Twelve", 13: "Thirteen", 14: "Fourteen", 15: "Fifteen", 16: "Sixteen", 17: "Seventeen", 18: "Eighteen", 19: "Nineteen"
        }
        
        numbers = [[0]*3 for i in range(4)]
        
        num = list(str(num))
        j = 3
        while num:
            i = 2
            while num and i > -1:
                numbers[j][i] = int(num.pop())
                i -= 1
            j -= 1
        
        ans = ""
        for i in range(len(numbers)):
            temp = ""
            for j in range(3):
                if numbers[i][j] != 0:
                    if j == 0:  temp += mapper[numbers[i][j]][0] + " Hundred "
                    elif j == 1:
                        if numbers[i][j] == 1:
                            cur = str(numbers[i][j]) + str(numbers[i][j+1])
                            temp += specialMapper[int(cur)] + " "
                            break
                        else:   temp += mapper[numbers[i][j]][1] + " "
                    elif j == 2:   temp += mapper[numbers[i][j]][0] + " "
            if temp != "":
                if i == 0:      ans += temp + "Billion "
                elif i == 1:    ans += temp + "Million "
                elif i == 2:    ans += temp + "Thousand "
                else:           ans += temp
        
        return ans[:-1]