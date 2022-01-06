class Solution:
    def romanToInt(self, s):
        rom = {"M":1000, "D":500, "C":100, "L":50, "X":10, "V":5, "I":1}
        int = 0
        for i in range(len(s)):
            if i > 0 and rom[s[i]] > rom[s[i-1]]:
                int += rom[s[i]]-2*rom[s[i-1]]        
            else:
                int += rom[s[i]]
        return int
                