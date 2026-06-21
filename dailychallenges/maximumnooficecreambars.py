class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        res = []
        sum = 0
        costs.sort()

        for i in range(len(costs)):
            if sum + costs[i] <= coins:
                res.append(i)
                sum += costs[i]

        return len(res)
#approach: greedy algorithm, sort the costs and keep adding until we reach the coins limit