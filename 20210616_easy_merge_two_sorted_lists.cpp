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
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        ListNode* answer = nullptr;
        ListNode* iterate = nullptr;
        
        if(l1 == nullptr)   return l2;
        if(l2 == nullptr)   return l1;
        
        if(l1->val < l2->val){
            answer = new ListNode(l1->val);
            l1 = l1->next;
        }else{
            answer = new ListNode(l2->val);
            l2 = l2->next;
        }
        iterate = answer;
        
        while(l1 != 0 && l2 != 0){
            ListNode* node_sm;
            if(l1->val < l2->val){
                iterate->next = new ListNode(l1->val);
                l1 = l1->next;
            }else{
                iterate->next = new ListNode(l2->val);
                l2 = l2->next;
            }
            
            iterate = iterate->next;
        }
        
        if(l1 != nullptr ){
            iterate->next = l1;   
        }
        if(l2 != nullptr){
            iterate->next = l2;
        }
        return answer;
    }
};
