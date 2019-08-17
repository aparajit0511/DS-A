class Solution:
    def prisonAfterNDays(self, a: List[int], N: int) -> List[int]:
        
        b = [-1,-1,-1,-1,-1,-1,-1,-1]
        i = 1
        while i <= N:

            if i > 1:
                a = b
                b = [-1,-1,-1,-1,-1,-1,-1,-1]

            if i > 0:
                b[0] = 0

            if a[len(a)-1] == 1 or a[len(a)-1] == 0:
                b[len(a)-1] = 0 

            for cell in range(1,len(a)-1):
                if a[cell-1] == 1 and a[cell+1] == 1:
                    b[cell] = 1
                elif a[cell-1] == 0 and a[cell+1] == 0:
                    b[cell] = 1
                elif a[cell-1] == 1 and a[cell+1] == 0:
                    b[cell] = 0
                elif a[cell-1] == 0 and a[cell+1] == 1:
                    b[cell] = 0

            i+=1

        return b