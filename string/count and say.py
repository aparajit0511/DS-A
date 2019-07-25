# Logic and Approach:
# I used two arrays count_array and seq_array. count_array to capture the sequence for the nth term and sequence array as an input array.
# Sequence array has a base input as "1", after that i calculate the sequence and append it to count_array.

class Solution:
    def countAndSay(self, n: int) -> str:
        # if n == 1:
        #     return "1"
        
        count_n = 1
        count_char = 1
        seq_array = []
        count_array = []
        for i in range(1):
            seq_array.append("1")
        
        # print(seq_array)
        
        while count_n < n:
            for i in range(0,len(seq_array)):
                if i+1 < len(seq_array):
                    if seq_array[i] == seq_array[i+1]:
                        count_char+=1
                        i+=1
                        continue;
                
                count_array.append(str(count_char))
                count_array.append(seq_array[i])
                count_char = 1
                i+=1
            
            seq_array = count_array
            count_array = []
            count_n+=1
            
        return ''.join(seq_array)
