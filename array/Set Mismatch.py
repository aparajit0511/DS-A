class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        
        sum_of_list = sum(nums)
        
        sum_of_nos_till_n = int((len(nums) + 1) * len(nums)/2)
        
        sum_of_list_without_repeat = sum(set(nums))
        
        # print(sum_of_list)
        # print(sum_of_nos_till_n)
        
        final_array = []
        
        final_array.append(sum_of_list - sum_of_list_without_repeat)
        
        final_array.append(sum_of_nos_till_n - sum_of_list_without_repeat)
        
        return final_array
        