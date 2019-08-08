class Solution:
    def intToRoman(self, num: int) -> str:
        
        Roman = {
        1 : 'I',
        4 : 'IV',
        5 : 'V',
        9 : 'IX',
        10 : 'X',
        40 : 'XL',
        50 : 'L',
        90 : 'XC',
        100 : 'C',
        400 : 'CD',
        500 : 'D',
        900 : 'CM',
        1000 : 'M'
        }

        Roman_list = []
        Roman_list.extend(Roman.keys())

        output = []

        while num > 0:

            for item in range(len(Roman_list)):
                if item+1 < len(Roman_list):
                    if Roman_list[item] <= num  and Roman_list[item+1] > num:
                        num = num - Roman_list[item]
                        output.append(Roman[Roman_list[item]])
                        break
                elif item+1 == len(Roman_list):
                    num = num - Roman_list[item]
                    output.append(Roman[Roman_list[item]])

        return ''.join(output)
