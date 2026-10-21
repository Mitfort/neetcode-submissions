# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists: return None 

        while len(lists) > 1:
            mergedLists = []

            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i+1] if i + 1 < len(lists) else None 
                mergedLists.append(self.mergeLists(l1,l2))
            
            lists = mergedLists
        return lists[0]
    
    def mergeLists(self,l1,l2):
        merged = ListNode()
        dummy = merged

        while l1 and l2: 
            if l1.val < l2.val: 
                dummy.next = l1
                l1 = l1.next 
            else:
                dummy.next = l2 
                l2 = l2.next
            
            dummy = dummy.next

        if l1: dummy.next = l1 
        if l2: dummy.next = l2

        return merged.next
        
        # if not lists: 
        #     return None

        # res = ListNode()
        # follow = res 
        # wasAdded = True

        # while wasAdded: 
        #     wasAdded = False 
        #     minVal = float('inf')
        #     idx = 0
            
        #     for i,l in enumerate(lists): 
        #         if l is None:
        #             continue
                
        #         if l.val < minVal: 
        #             minVal = l.val
        #             idx = i
        #             wasAdded = True 
            
        #     if not wasAdded:
        #         break
            
        #     save = lists[idx].next
        #     follow = lists[idx]
        #     follow.next= 
        #     lists[idx] = save 

        # return res.next

                
    
                