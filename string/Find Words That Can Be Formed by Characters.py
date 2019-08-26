class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:

        real_count = 0
        from collections import Counter

        counter_chars = Counter(chars)

        for word in words:
            counter_word = Counter(word)

            count = 0
            for key,value in counter_word.items():
                if key not in counter_chars.keys():
                    break
                elif key in counter_chars.keys() and value <= counter_chars[key]:
                    count+=value
                else:
                    break

            if count == len(word):
                real_count+=count

        return real_count