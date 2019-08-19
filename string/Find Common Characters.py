class Solution:
    def commonChars(self, words: List[str]) -> List[str]:

        alphabet = {"a":200,"b":200,"c":200,"d":200,"e":200,
                   "f":200,"g":200,"h":200,"i":200,"j":200,
                   "k":200,"l":200,"m":200,"n":200,"o":200,
                   "p":200,"q":200,"r":200,"s":200,"t":200,
                   "u":200,"v":200,"w":200,"x":200,"y":200,"z":200}

        count = 0
        cur_count = 0

        for word in words:
            for w in word:
                if w not in alphabet.keys():
                    continue
                else:
                    cur_count = word.count(w)
                    alphabet[w] = min(alphabet[w],cur_count)

            count+=1

            if count == 1:
                alphabet = dict(filter(lambda x:x[1]<200,alphabet.items()))

            if count > 1:
                alpha = {}
                alpha = alphabet.copy()
                for key in alpha.keys():
                    if key not in word:
                        alphabet.pop(key)
                # alphabet = alpha.copy()


        result = []
        for key in alphabet.keys():
                for i in range(alphabet[key]):
                    result.append(key)

        return result