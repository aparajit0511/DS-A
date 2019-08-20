class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        freq_pattern = {}
        
        result = []
        pattern_sum = 0
        

        for c in str(pattern):
            freq_pattern[c] = str(pattern).count(c)

        for value in freq_pattern.values():
            pattern_sum*=10
            pattern_sum+=value


        for word in words:
            if len(word) != len(pattern):
                continue
            else:
                word_sum = 0
                freq_word = {}
                for w in word:
                    freq_word[w] = str(word).count(w)
                # print(freq_word)

                for value in freq_word.values():
                    word_sum*=10
                    word_sum+=value

                if word_sum == pattern_sum:
                    result.append(word)

        return result

Test Cases: 43/46

Input:       ["badc","abab","dddd","dede","yyxx"]
              "baba"

Output:      ["abab","dede","yyxx"]

Expected:    ["abab","dede"]