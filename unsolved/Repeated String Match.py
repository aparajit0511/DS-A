class Solution:
    def repeatedStringMatch(self, A: str, B: str) -> int:
        a = 'abcd'
        b = 'dbcadbcad'
        a = list(A)
        b = list(B)
        count = 0

        if len(a) > len(b):
            for letter in range(len(a)):
                if b[letter:len(b)] == a[letter:len(b)]:
                    return 0
            return -1 
        else:
            while len(a) <= len(b):
                
                for letter in range(len(a)):
                    if b[letter:len(b)] == a[letter:len(b)]:
                        return count

                a.extend(a)
                count+=1

        return -1