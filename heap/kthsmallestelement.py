import heapq
def smallest(nums,k):
    heapq.heapify(nums)
    new = []
    for _ in range(k):
        minn = heapq.heappop(nums)
        new.append(minn)
    return new