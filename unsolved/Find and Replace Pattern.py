class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        freq_pattern = {}
        
        result = []

        for c in str(pattern):
            freq_pattern[c] = str(pattern).count(c)
        freq_pattern = dict(freq_pattern)
        freq_pattern = sorted(freq_pattern.items(),key = lambda x:x[1])

        for word in words:
            if len(word) != len(pattern):
                continue
            else:
                freq_word = {}
                for w in word:
                    freq_word[w] = word.count(w)
                freq_word = dict(freq_word)
                freq_word = sorted(freq_word.items(),key = lambda x:x[1])

                count = 0

                for key,value in freq_word.items():
                    if value == freq_pattern[key]:
                        count+=1
                    else:
                        break

                if count == len(freq_pattern):
                    result.append(word)

        return result

