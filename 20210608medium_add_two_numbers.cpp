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
        int pass = 0;
        ListNode* result = nullptr;
        ListNode* answer = nullptr;

        while(l1!=nullptr || l2!=nullptr || pass>0){
            int val1, val2;
            if(l1 == nullptr){
                val1 = 0;
            }else{
                val1 = l1->val;
                l1 = l1->next;
            }
            
            if(l2 == nullptr){
                val2 = 0;
            }else{
                val2 = l2->val;
                l2 = l2->next;
            }
            
            int sum = val1 + val2 + pass;
            int keep = sum%10;
            pass = (sum-keep)/10;
            
            if(answer == nullptr){
                answer = new ListNode(keep);  // keep head
                result = answer;
	        }else{
                result->next = new ListNode(keep);
                result = result->next;
            }
            
        }
        
        return answer;
    }
};
