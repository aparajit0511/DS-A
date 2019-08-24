class Solution:
    def frequencySort(self, s: str) -> str:
        
        result = []
        freq_word = {}
        
        len(s)
        
        from collections import Counter
        
        counter = Counter(s)
        # print(counter)
            
        counter = dict(sorted(counter.items(),key=lambda x:x[1],reverse = True))
        
        for key in counter.keys():
            for i in range(counter[key]):
                result.append(key)
            
        return ''.join(result)
        