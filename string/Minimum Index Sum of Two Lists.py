class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        
        sum_of_index = 0
        min_sum = 2000
        restaurant = []

        for item in range(len(list1)):
            if list1[item] in list2:
                sum_of_index = item + list2.index(list1[item])

                if sum_of_index <= min_sum and list1[item] not in restaurant:
                    restaurant.append(list1[item])
                    min_sum = min(sum_of_index,min_sum)


        return restaurant