#my solution
class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        val = max(nums)-min(nums)
        count = 0
        for i in range(k):
            count += val
        return count 