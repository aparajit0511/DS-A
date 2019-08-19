class Solution:
    def isHappy(self, n: int) -> bool:
        
        # result = []
        
        sum = happy(n)
        # result.append(sum)
        n = sum
        t = 10
        
        while t != 0 :
            if sum != 1:
                sum = happy(n)
                # result.append(sum)
                # print("hi")
                n = sum
            else:
                return True
            t-=1
            
        return False
    
def happy(n):
    sum = 0
    while n > 0:
        x = n % 10
        sum = sum + (x*x)
        n = int(n / 10)
    
    # print(sum)
    return sum
        