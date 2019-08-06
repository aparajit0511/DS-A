class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        if len(ransomNote) == 0:
            return True
        
        for letter in ransomNote:
            count_of_letter = ransomNote.count(letter)
            if letter in magazine:
                if count_of_letter < magazine.count(letter) or count_of_letter == magazine.count(letter):
                    continue
                else:
                    return False
            else:
                return False
            
        return True