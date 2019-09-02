### N^2 Solution

class Solution:
    def maxScoreSightseeingPair(self, A: List[int]) -> int:

        hash_table = []
        value = 0
        max_value = 0

        for item in range(1,len(A)):
            hash_table.append(item)

        for item in range(len(A)-1):
            for j in range(len(hash_table)):
                if max_value > A[item]+A[hash_table[j]]:
                    continue
                else:
                    value = A[item] + A[hash_table[j]] + item - hash_table[j]
                    max_value = max(max_value,value)
            hash_table.remove(item+1)

        return max_value

### 2N Solution

class Solution:
    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        max_value = []
        max_value.append(0)
        max_pair = []
        max_pair.append(0)

        for i in range(1,len(A)):
            max_value.append(max(max_value[i-1],A[i-1] + (i-1)))

        score = 0

        for i in range(1,len(A)):
            score = max_value[i] + A[i] - i
            max_pair.append(max(score,max_pair[i-1]))

        return max(max_pair)
