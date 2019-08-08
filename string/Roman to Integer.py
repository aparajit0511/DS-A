class Solution:
    def romanToInt(self, s: str) -> int:
        
        Roman = {
        'I' : 1,
        'V' : 5,
        'X' : 10,
        'L' : 50,
        'C' : 100,
        'D' : 500,
        'M' : 1000
        }
        
        RomanSpecial = {
            'IV' : 4,
            'IX' : 9,
            'XL' : 40,
            'XC' : 90,
            'CD' : 400,
            'CM' : 900
        }

        sum = 0
        i = 0

        while i < len(list(s)):
                if i+1 < len(list(s)) and s[i] + s[i+1] in RomanSpecial:
                    sum = sum + RomanSpecial[s[i]+s[i+1]]
                    i=i+2
                elif s[i] in Roman and i+1 < len(list(s)) and s[i] + s[i+1] not in RomanSpecial:
                    sum = sum + Roman[s[i]]
                    i+=1
                else:
                    sum = sum + Roman[s[i]]
                    i+=1
            
            # print(f"sum is:{sum}")        
            # print(f"i is {i}")
        return sum