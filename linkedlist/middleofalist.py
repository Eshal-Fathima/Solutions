#use fast and slow pointer to find the middle of a linked list
#slow == move 1 space 
#fast == move 2 spaces
#slow + 1 == fast + 2

class Node:
    def __init__(self, val = 0, next = none):
        self.val = val
        self.next = next
class Solution:
    def middle(self,head):
        slow, fast = head,head
        while fast and fast.next:
            slow = slow.next 
            fast = fast.next.next
        return slow

#uses 2 pointer technique
