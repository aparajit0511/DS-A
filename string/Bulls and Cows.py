class Solution:
    def getHint(self, s: str, g: str) -> str:
        secret = list(s)
        guess = list(g)
        
        bulls = 0
        cows = 0

        count_array = [0,0,0,0,0,0,0,0,0,0]

        for item in range(len(secret)):
            count_array[int(secret[item])]+=1
        print(count_array)

        for item in range(len(guess)):
            if count_array[int(guess[item])] > 0:
                if guess[item] == secret[item]:
                    bulls+=1
                    count_array[int(guess[item])]-=1
                
        
        for item in range(len(guess)):
            if count_array[int(guess[item])] > 0:
                if guess[item] != secret[item]:
                    cows+=1
                    count_array[int(guess[item])]-=1

        return ''.join(str(bulls)+"A"+str(cows)+"B")