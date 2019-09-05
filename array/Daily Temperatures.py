## Working solution

class Solution(object):
    def dailyTemperatures(self, T):
        ans = [0] * len(T)
        print(ans)
        stack = [] #indexes from hottest to coldest
        for i in range(len(T) - 1, -1, -1):
            while stack and T[i] >= T[stack[-1]]:
                stack.pop()
            if stack:
                print(stack[-1])
                ans[i] = stack[-1] - i
            stack.append(i)
        return ans



class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        
        
        result = []
        count = 0
            
        for item in range(len(T)-1):

            if T[item] < T[item+1]:
                count+=1
            else:
                mark = item+1

                while mark < len(T):
                    if T[item] > T[mark] and mark == len(T)-1:
                        count = 0
                        break
                    elif T[item] < T[mark]:
                        count+=1
                    else:
                        count+=1
                        break
                    mark+=1

            result.append(count)

            
        result.append(0)
        
        return result


class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        stack = {}
        ans = []
        top = 0

        for i in reversed(range(len(T))):

            if len(stack)==0:
                stack.update({T[i]:i})
                ans.append(0)
                top+=1
            else:
                stack_ele = list(stack.keys())
                print(stack_ele)
                while  stack_ele[-1] <= T[i]:
                    if len(stack) == 0:
                        break
                    stack.pop(stack_ele[-1])
                    top=-1
                
                ans.append(stack[stack_ele[-1]] - i)
                print(stack[stack_ele[-1]])
                stack.update({T[i]:i})
                top+=1

        print(reversed(ans))

        return reversed(ans)