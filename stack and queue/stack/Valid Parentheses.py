class Solution:
    def isValid(self, s: str) -> bool:
        
        if len(s) == 0:
            return True
        
        if len(s) % 2 == 1:
            return False
        
        stack = []
        top = -1
        i = 0

        mapping = {"{":"}","[":"]","(":")"}

        while i < len(s)-1:
            if mapping.get(s[i]) == s[i+1]:
                i=i+2
                continue
            else:
                if len(stack) == 0:
                    stack.append(s[i])
                    top+=1
                else:
                    if mapping.get(stack[top]) == s[i]:
                        stack.pop()
                        top-=1
                    else:
                        stack.append(s[i])
                        top+=1

            i=i+1

        if len(stack) == 0:
            return True
        elif len(stack) == 1:
            if mapping.get(stack[top]) == s[len(s)-1]:
                return True

        return False