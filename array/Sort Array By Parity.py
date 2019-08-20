class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        
        result1 = []
        result2 = []
        
        for item in A:
            if item % 2 == 0:
                result1.append(item)
            else:
                result2.append(item)
        # print(result1,result2)
        
        result1.extend(result2)
                
        return result1
        