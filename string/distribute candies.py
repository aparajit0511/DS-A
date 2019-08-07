class Solution:
    def distributeCandies(self, candies: List[int]) -> int:

        sis_count = (len(candies)/2)-1
        candy_count = 0
        sis = []

        for candy in range(len(set(candies))):
            if candy_count < sis_count or candy_count == sis_count:
                candy_count+=1
                sis.append(candies[candy])
            else:
                break


        return len(sis)
