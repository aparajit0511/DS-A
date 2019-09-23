class Solution:
    def reverseWords(self, s: str) -> str:
        
        # print(''.join(s.split().reverse()))
        
        s = s.split()
        s.reverse()
        return ' '.join(s)
        