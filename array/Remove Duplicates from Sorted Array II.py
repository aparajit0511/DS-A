class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        i, j= 0, 2
        while i<len(nums) and j< len(nums):
            if nums[i]==nums[j]:
                nums.remove(nums[i])
                
            else:
                i+=1
                j+=1
        return len(nums)
        