class Solution:
    def romanToInt(self, s: str) -> int:
        dic = {"M":1000, "D":500, "C":100, "L":50, "X":10, "V":5, "I":1}
        result = 0
        for i in range(len(s)-1): 
            num = dic[s[i]] # 왼쪽 
            nextnum = dic[s[i+1]] # 오른쪽
            if(num>=nextnum): #왼쪽 수가 더 크면 그냥 더함 
                result += num
            else(num<=nextnum):
                result -= num
                  
        result += dic[s[len(s)-1]]
        return(result)
                