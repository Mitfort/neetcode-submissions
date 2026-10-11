# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None:
            return False

        if head.next == None:
            return False
        
        pointer = head
        index = 1;

        while pointer: 
            if pointer == None:
                return False

            if pointer.next == None:
                return False
            
            if pointer.val < index:
                return True

            pointer.val = index
            index+=1

            pointer = pointer.next
        
        return False





            