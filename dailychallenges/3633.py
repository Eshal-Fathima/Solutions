#earliest finish time for land and water
class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        res = []
        for i in range(len(landStartTime)):
            for j in range(len(waterStartTime)):
                land = landStartTime[i]+landDuration[i]
                if land > waterStartTime[j]:
                    res.append(land + waterDuration[j])
                else:
                    bal = waterStartTime[j] - land
                    res.append(land + bal + waterDuration[j])
        for i in range(len(waterStartTime)):
            for j in range(len(landStartTime)):
                water = waterStartTime[i]+waterDuration[i]
                if water > landStartTime[j]:
                    res.append(water + landDuration[j])
                else:
                    bal = landStartTime[j] - water
                    res.append(water + bal + landDuration[j])
        return min(res)
    
# approach: brute force method
# could have used a more efficient method by sorting the start times
# then using two pointers to find the earliest finish time.
# what i did was to iterate through all possible combinations of land and water start times
# calculate the finish time for each combination
# then return the minimum finish time.