# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        length:int = 0
        ptr = head 

        while ptr: 
            length += 1 
            ptr = ptr.next 

        idx_to_remove = length - n + 1
        curr_idx = 0

        prev = None 
        curr = head 

        while curr:
            curr_idx +=1 

            if curr_idx == idx_to_remove:
                if prev == None: 
                    return curr.next

                prev.next = curr.next 
                break 
            
            temp = curr 
            curr = curr.next 
            prev = temp 
        
        return head

    


