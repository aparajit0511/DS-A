class Solution:
    def getHint(self, s: str, g: str) -> str:
        

        secret = list(s)
        guess = list(g)

        bulls = 0
        cows = 0

        for number in range(len(secret)):
            if secret[number] == guess[number] and secret.index(secret[number]) == guess.index(guess[number]):
                bulls+=1
            elif secret[number] in guess:
                cows+=1

        print(bulls,cows)

        return ''.join(str(bulls)+"A"+str(cows)+"B")



class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        

        # secret = list(s)
        # guess = list(g)

        bulls = 0
        cows = 0

        for i in guess:
            if i in secret and guess.index(i) == secret.index(i):
                bulls+=1
                secret = secret.replace(i,' ',1)
            elif i in secret:
                cows+=1
                secret = secret.replace(i,' ',1)
                
        print(secret)
            
            

        # print(bulls,cows)

        return ''.join(str(bulls)+"A"+str(cows)+"B")