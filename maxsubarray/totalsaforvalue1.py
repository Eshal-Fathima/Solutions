#my solution
class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        val = max(nums)-min(nums)
        count = 0
        for i in range(k):
            count += val
        return count 
    
# brute force method or direct computation method
# time complexity = O(n+k)
# space complexity = O(1)

# more optimized version 
class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        return (max(nums)-min(nums))*k
    
# time complexity = O(n)
# space complexity = O(1)
# approach: Brute force or direct approach