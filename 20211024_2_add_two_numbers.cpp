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
        ListNode pre(0), *p= &pre;
        int empty = 0;
        while(l1 || l2 || empty){
            if(l1)  empty += l1->val, l1 = l1->next;
            if(l2)  empty += l2->val, l2 = l2->next;
            
            p->next = new ListNode(empty%10);
            empty /= 10;
            
            p = p->next;
        }
        
        return pre.next;
    }
};
