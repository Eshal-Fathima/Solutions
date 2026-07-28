#my solution
class Solution:
    def maxTotalValue(self, nums, k: int) -> int:
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
    def maxTotalValue(self, nums, k: int) -> int:
        return (max(nums)-min(nums))*k
    
# time complexity = O(n)
# space complexity = O(1)
#maxsubarray uses kadens algorithm to find the maximum sum of a contiguous subarray. The approach is to iterate through the array and keep track of the current sum and the maximum sum found so far. If the current sum becomes negative, reset it to zero. The maximum sum will be the answer at the end of the iteration.
# approach: Brute force or direct approach