class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = 0
        
        for item in range(len(nums)):
            if nums[item] != 0:
                nums[count] = nums[item]
                count+=1
                
        for item in range(count,len(nums)):
            nums[item] = 0
            
        print(nums)
        
### With Extra Space
        
        zeroes = []
        count = 0
        
        for item in nums:
            if item == 0:
                count+=1
            else:
                zeroes.append(item)
                
        for item in range(count):
            zeroes.append(0)
          
        print(zeroes)
        nums = zeroes[:]
        print(nums)
        