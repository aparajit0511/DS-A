class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        
        result = []

        import collections

        counter = collections.Counter(nums)

        for key in counter.keys():
            if counter[key] == 2:
                result.append(key)

        return result
        