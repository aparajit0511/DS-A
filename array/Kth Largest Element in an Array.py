class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        nums.sort(reverse=True)
        print(nums)
        i = 1
        
        while i< k:
            i+=1
            
        print(i)
        return nums[i-1]
        