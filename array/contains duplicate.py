class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        if len(nums) - len(set(nums)) == 0:
            return False
        return True
        