class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    def mergeTwoLists(self, list1: Node, list2: Node) -> Node:
        dummy = Node(0)     #created a dummy list that starts with 0
        tail = dummy        #tail as a ptr so that it can move throught the list
        
        while list1 and list2:
            if list1.data < list2.data:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2
        
        return dummy.next