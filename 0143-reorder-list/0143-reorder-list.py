# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        slow = head
        fast = head.next
        #find middle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next


        second=slow.next
        slow.next=None
        prev=None 
        #reverse
        while second:
            temp=second.next
            second.next=prev
            prev=second
            second=temp 
        #merge
        second =prev
        first=head
        while second:
            temp1,temp2= first.next,second.next
            first.next= second
            second.next=temp1
            first, second =temp1,temp2


             

            



        





        
