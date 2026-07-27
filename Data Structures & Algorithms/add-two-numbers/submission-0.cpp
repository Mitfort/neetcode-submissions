/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        
        ListNode res;
        ListNode* ptr = &res; 
        int rest = 0;

        while(l1 || l2 || rest)
        {
            int x = l1 ? l1->val : 0;
            int y = l2 ? l2->val : 0;  
            
            int sum = x + y + rest;

            rest = sum / 10;

            ptr->next = new ListNode(sum % 10);
            ptr = ptr->next;

            if(l1) l1 = l1->next;
            if(l2) l2 = l2->next;
        }

        return res.next;

    }
};
