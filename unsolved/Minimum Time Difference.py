class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:

        for time in timePoints:

            if time[0:2] == "00" and time[3:5] == "00":
                curr_time = 24
            elif time[0:2] == "00" and int(time[3:5]) > 0 and int(time[3:5]) <= 59:
                curr_time = 0
            elif time[0:2] != "00":
                curr_time = int(time[0:2])
            curr_time*=60
            minutes = int(time[3:5])
            curr_time+=minutes

            timePoints[timePoints.index(time)] = curr_time
            # curr_time = 0


        timePoints = sorted(timePoints,reverse=True)
        print(timePoints)

        count = 0
        min_time = 1500         #as max time difference will be approx 1500

        prev_time = timePoints[0]
        timePoints = timePoints[1:len(timePoints):]

        for time in timePoints:

            curr_time = time

            min_time = min(min_time,prev_time - curr_time)
            print("prev_time",prev_time,"curr_time",curr_time)
            prev_time = curr_time
            
            count+=1

            if count == len(timePoints):
                break


        return min_time

["05:31","22:08","00:35"]
296
147