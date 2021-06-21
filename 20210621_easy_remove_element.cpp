class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        queue<int> ind;
        int k = 0;
        int index=0;
        
        for(int num: nums){
            // cout << num;
            if(num == val){
                ind.push(index);
            }else{
                k++;
                int empty;
                if(ind.size()!=0){
                    empty = ind.front();
                    ind.pop();
                }else{
                    empty = k+1;
                }
                nums[min(empty, k-1)] = num;
            }
            index++;
        }
        return k;
    }
};
