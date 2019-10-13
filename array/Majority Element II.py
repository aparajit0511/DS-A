class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        result = []
        
        for i in nums:
            count  = nums.count(i)
            if count > len(nums)/3:
                result.append(i)
                
        return set(result)
                
        