class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        
        mark1 = []
        mark2 = []
        
        for item in range(len(A)):
            if item % 2 == 0:
                if A[item] % 2 != 0:
                    mark1.append(item)
            else:
                if A[item] % 2 != 1:
                    mark2.append(item)
                    
            if len(mark1) != 0 and len(mark2) != 0:
                A[mark1[-1]],A[mark2[-1]] = A[mark2[-1]],A[mark1[-1]]
                mark1.pop()
                mark2.pop()
        
        
        return A
        