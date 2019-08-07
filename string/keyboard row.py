class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        
        keywords = ["qwertyuiopQWERTYUIOP","asdfghjklASDFGHJKL","zxcvbnmZXCVBNM"]

        valid_words = []

        for word in words:
            if all([letter in keywords[0] for letter in word]) is True:
                valid_words.append(word)
            elif all([letter in keywords[1] for letter in word]) is True:
                valid_words.append(word)
            elif all([letter in keywords[2] for letter in word]) is True:
                valid_words.append(word)


        return valid_words