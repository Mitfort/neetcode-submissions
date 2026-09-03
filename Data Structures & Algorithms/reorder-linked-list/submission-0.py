# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        # Find middle 
        slow,fast = head,head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second = slow.next
        slow.next = None

        # Reverse second half

        prev = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp 

        # Merge
        first, second = head, prev
        while second:
            tmp1,tmp2 = first.next,second.next

            first.next = second
            second.next = tmp1

            first = tmp1
            second = tmp2

        


#----------------------
        # forward = head
        # backward = head 
        # curr = head
        # self.backOrder = []

        # def goDown(ptr):
        #     if ptr == None:
        #         return

        #     goDown(ptr.next.next)

        #     self.backOrder.append(ptr)

        # goDown(backward)

        # for ptr in self.backOrder:
        #     print(ptr.val)

        # swap = True
        # idx = 0
        # head = curr
        
        # while curr:
        #     if swap:
        #         if idx >= len(self.backOrder):
        #             curr.next = None
        #             break

        #         curr.next = self.backOrder[idx]
        #         idx+=1
        #         swap = False
        #     else:
        #         curr.next = forward
        #         forward = forward.next
        #         swap = True


        #     curr = curr.next 

        
        
            