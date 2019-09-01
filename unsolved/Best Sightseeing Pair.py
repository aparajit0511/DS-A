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