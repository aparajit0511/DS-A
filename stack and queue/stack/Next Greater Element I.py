class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        ans = []

        for item in range(len(nums1)):
            if nums1[item] in nums2:
                item_index = nums2.index(nums1[item])
                element_exist  = 0
                for i in  range(item_index,len(nums2)):
                    if i+1 != len(nums2):
                        if nums1[item] < nums2[i+1]:
                            ans.append(nums2[i+1])
                            break
                        elif element_exist == (len(nums2) - item_index+1):
                            ans.append(-1)
                    else:
                        ans.append(-1)
                    element_exist+=1

        return ans
