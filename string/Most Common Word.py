class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        
        count_words = dict()

        import string
        # paragraph = "".join(l=l+"" for l in paragraph if l not in string.punctuation)
        
        new_string = ""
        
        for l in paragraph:
            if l in string.punctuation:
                new_string+=" "
            else:
                new_string+=l

        paragraph = new_string.lower().split()

        for word in paragraph:
            if word not in count_words and word not in banned:
                count_words[word] = 1
            elif word in count_words:
                count_words[word]+=1

        max_value = 0

        for key in count_words.keys():
            if count_words[key] > max_value:
                max_value = count_words[key]
                max_key = key
        print(count_words)

        return max_key