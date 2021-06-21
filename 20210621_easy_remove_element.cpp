class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        queue<int> ind;
        int k = 0;
        int index=0;
        
        for(int num: nums){
            if(num == val){
                ind.push(index);
            }else{
                k++;
                if(ind.size()!= 0){
                    int i = ind.front();
                    ind.pop();
                    nums[i] = num;
                }else{
                    nums[k-1] = num;
                }
            }
            index++;
        }
        return k;
    }
};
