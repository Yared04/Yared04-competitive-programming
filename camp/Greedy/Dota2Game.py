class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        rs,ds = 0,0
        bannedR, bannedD = 0,0
        for char in senate:
            if char == "R":
                rs+= 1
            elif char == "D":
                ds+= 1
        while True:
            for i in range(len(senate)):
                if i < len(senate) and senate[i] == "R":
                    if not bannedR:
                        if ds < 1:
                            return "Radiant"
                        else:
                            ds -= 1
                            bannedD += 1
                    else:
                        senate = senate[:i] + " " + senate[i+1:]
                        bannedR -= 1 
                        continue
                elif i < len(senate) and senate[i] == "D":
                    if not bannedD:
                        if rs < 1:
                            return "Dire"
                        else:
                            rs -= 1
                            bannedR += 1
                    else:
                        senate = senate[:i] + " " + senate[i+1:]
                        bannedD -= 1
                        continue
                