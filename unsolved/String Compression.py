class Solution:
    def compress(self, chars: List[str]) -> int:
        
        new_chars = []

        for item in set(chars):
            word_count = chars.count(item)
            new_chars.append(item)

            if word_count > 9:
                quotient = word_count / 10
                remainder = word_count % 10
                new_chars.append(str(quotient))
                new_chars.append(str(remainder))
            else:
                new_chars.append(str(word_count))

        return len(new_chars)