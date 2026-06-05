import heapq

class Solution:
    def findKthLargest(self, nums, k):
        heap = nums[:k]
        heapq.heapify(heap)

        for x in nums[k:]:
            if x > heap[0]:
                heapq.heapreplace(heap, x) 
        # The root is the k-th largest element
        return heap[0]