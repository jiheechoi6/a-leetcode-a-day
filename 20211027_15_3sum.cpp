class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        if(nums.size() == 0)    return vector<vector<int>> {};
        
        sort(nums.begin(), nums.end());
        
        int last_idx = nums.size()-1;
        vector<vector<int>> out;
        
        for(int i=0; i<last_idx-1; i++){
            if(i!=0 && nums[i]==nums[i-1])  continue;
            
            int start = i+1, end = last_idx;
            int sum_2 = nums[start] + nums[end], sum_2_target = 0-nums[i];
            
            while(start<end){
                if(sum_2<sum_2_target){
                    start++;
                }else if(sum_2>sum_2_target){
                    end--;
                }else{
                    if(start==i+1 || nums[start]!=nums[start-1])
                        out.push_back(vector<int> {nums[i], nums[start], nums[end]});
                    start++;
                }
                sum_2 = nums[start]+nums[end];
            }
        }
        return out;
    }
};
