class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        result = []
        
        from collections import Counter
        from collections import OrderedDict
        
        counter = Counter(nums)
        counter = dict(sorted(counter.items(),key=lambda x:x[1],reverse = True))
        print(counter)
        count_element = 0
        
        for key,value in counter.items():
            print(key)
            if count_element < k:
                result.append(key)
            count_element+=1
                
        return result
        