# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        counter1: int = 0
        counter2: int = 0
        if head == None:
            return head

        if head.next == None and n > 0: 
            return None

        ptr = head

        while ptr:
            counter1+=1
            ptr = ptr.next

        ptr = head
        counter2 = counter1 - n
        counter1 = 0
        

        while ptr:
            if counter1 == counter2:
                head = ptr.next
                break

            if counter1+1 == counter2:
                ptr.next = ptr.next.next
                break

            counter1+=1
            ptr = ptr.next

        return head



        