class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        hash_s = {}
        hash_t = {}
        
        for i in s:
            hash_s[i] = s.count(i)
            
        for j in t:
            hash_t[j] = t.count(j)
        
        print(hash_s,hash_t)
        for key,value in hash_t.items():
            if key in hash_s:
                if hash_s[key] < hash_t[key]:
                    break
            elif key not in hash_s:
                break
                
        return key
        