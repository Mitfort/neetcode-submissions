# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return 
            
        # Devide the list
        l1 = head 
        l2 = head.next 

        while l2 and l2.next: 
            l2 = l2.next.next
            l1 = l1.next 
        
        # Start on the second half and brake connection
        l2 = l1.next
        l1.next = None 

        # Reverse the second list
        prev = None
        curr = l2

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp 

        # Merge both lists 
        new = head

        while prev:
            tmp1,tmp2 = new.next, prev.next
            new.next = prev
            prev.next = tmp1
            new, prev = tmp1, tmp2 
         
