class Solution:
    def firstUniqChar(self, s: str) -> int:
        list_s = list(s)        
        
        for character in set(s):
            list_s.remove(character)
            
        for letter in range(len(s)):
            if s[letter] not in list_s:
                return letter
        
        return -1
        