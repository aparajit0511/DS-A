class Solution:
    def duplicateZeros(self, lst: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        i = 0
        while i < len(lst):
            if lst[i] == 0:
                lst.insert(i+1,0)
                lst.pop()
                i+=2
            else:
                i+=1
            
        return None