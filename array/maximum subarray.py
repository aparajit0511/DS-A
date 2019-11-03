class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        
        # if cum_sum < 0 then reset the start element to next element and cumsum = 0

        cum_sum = 0
        max_value = -99999999999
        
        item = 0

        while item < (len(nums)):
            # print(nums[item])
            cum_sum += nums[item]
            if cum_sum < nums[item] :
                cum_sum = 0
                # item-=1
                continue
            
            max_value = max(max_value,cum_sum)
            item+=1    
            print(cum_sum)


        return max_value
