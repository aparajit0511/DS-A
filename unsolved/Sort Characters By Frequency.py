class Solution:
    def frequencySort(self, s: str) -> str:
        
        result = []
        freq_word = {}
        
        len(s)
        
        for item in s:
            freq_word[item] = s.count(item)
            
        freq_word = dict(sorted(freq_word.items(),key=lambda x:x[1],reverse = True))
        
        for key in freq_word.keys():
            for i in range(freq_word[key]):
                result.append(key)
            
        return ''.join(result)
        

Test Case: 33/36