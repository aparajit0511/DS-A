class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        
        jewel_count = 0
        for stone in S:
            if stone in J:
                jewel_count+=1
                
        return jewel_count
        