class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        
        replica_text = text.split()

        third = []

        for item in range(len(replica_text)-2):
            if replica_text[item] == first and replica_text[item+1] == second:
                third.append(replica_text[item+2])

        return third