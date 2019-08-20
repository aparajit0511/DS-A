class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        
        nums1 = sorted(nums)
        
        sum = min(nums1[0],nums1[1])
        i = 2
        while i < len(nums1):
            if i+1 <= len(nums1)-1:
                sum+=min(nums1[i],nums1[i+1])
            i=i+2
                    
        return sum
        