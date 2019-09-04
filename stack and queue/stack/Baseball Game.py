class Solution:
    def calPoints(self, ops: List[str]) -> int:
        
        top = -1
        valid_points = []
        score = 0

        for point in ops:
            if point == "C":
                score-=valid_points[top]
                valid_points.pop()
                top-=1

            elif point == "D":
                if len(valid_points) > 0:
                    score = score + (2 * valid_points[top])
                    valid_points.append(2*valid_points[top])
                    top+=1

            elif point == "+":
                if len(valid_points) >=2:
                    final_point = valid_points[top] + valid_points[top-1]
                    score+=final_point
                    valid_points.append(final_point)
                    top+=1
                    
            else:
                score+=int(point)
                valid_points.append(int(point))
                top+=1

        return score