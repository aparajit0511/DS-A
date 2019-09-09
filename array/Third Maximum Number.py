class Solution:
    def thirdMax(self, nums: List[int]) -> int:

        nums = list(set(nums))

        if len(nums) < 3:
            return max(nums)
        else:
            
            max_no = nums[0]
            
            for i in range(1,len(nums)):
                if nums[i] > max_no:
                    max_no = nums[i]
            
            nums.remove(max_no)

            second = nums[0]

            for i in range(1,len(nums)):
                if nums[i] > second and nums[i] < max_no:
                    second = nums[i]
                    
            nums.remove(second)
            third = nums[0]
            
            for i in range(1,len(nums)):
                if nums[i] > third and nums[i] < second and nums[i] < max_no:
                    third = nums[i]

            return third