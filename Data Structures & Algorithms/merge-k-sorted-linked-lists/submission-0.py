# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        n_lists = len(lists)
        
        if n_lists <= 0:
            return None

        group = []
        for l in lists:
            curr = l
            while curr:
                group.append(curr.val)
                curr = curr.next

        if len(group) == 0:
            return None
            
        group.sort()

        head = ListNode()
        curr = head

        for i in range(len(group) - 1):
            curr.val = group[i]
            curr.next = ListNode()
            curr = curr.next

        curr.val = group[-1]
        curr.next = None

        return head 

    