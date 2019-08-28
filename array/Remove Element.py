class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        for item in sorted(nums):
            if item == val:
                nums.remove(item)
                
        print(nums)
        
        return len(nums)
        