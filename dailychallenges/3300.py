# Minimum element after replacing with digit 

# basically add the numbers in the list order by order
# and find the minimum of that number
# eg : 10 == 1+0 = 1
 
class Solution:
    def minElement(self, nums: List[int]) -> int:
        ans = float('inf')            #gives infinity value so that it is not = 0 meaning
        #number given will be always greater than the given current number == infinity
        for i in nums:
            res = 0
            while i:        #while i is not equal to 0 is the condition here 
                res += i % 10
                i = i // 10
            ans = min(res, ans)     #compares the res of the digits, and answer gives you 
            # the minimum value among them
        return ans