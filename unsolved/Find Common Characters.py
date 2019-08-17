class Solution:
    def commonChars(self, A: List[str]) -> List[str]:

        common_words = []

        for word in A:
            for letter in word:
                if any(letter in A for letter in word) is True:
                    common_words.append(letter)

        return set(common_words)