# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        slow=head
        fast=head
        c=0
        while fast and fast.next:
            if c!=0 and slow==fast:
                return True
            slow=slow.next
            fast=fast.next.next
            c+=1

        return False


        