class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        
        morse_code = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        
        alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
        
        code = dict(zip(alphabet,morse_code))
        
        final_morse_code = []
        
        for i in words:
            final = []
            for j in i:
                if j in code.keys():
                    final.append(code[j])
            final_morse_code.append(''.join(final))
        
        return len(set(final_morse_code))
        