class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        visited = {}
        for i in range(len(nums)):
            if target - nums[i] in visited:
                return [visited[target - nums[i]][0], i]
            if nums[i] in visited:
                visited[nums[i]].append(i)
            else:
                visited[nums[i]] = [i]