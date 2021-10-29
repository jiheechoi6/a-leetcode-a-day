class Solution {
public:
    int threeSumClosest(vector<int>& nums, int target) {
        sort(nums.begin(), nums.end());
        int last_idx = nums.size()-1, res = nums[0]+nums[1]+nums[2];
        
        for(int i=0; i<last_idx-1; i++){
            int start = i+1, end = last_idx;
            while(end>start){
                int sum = nums[i] + nums[start] + nums[end];
                if(sum>target){
                    end--;
                }else if(sum<target){
                    start++;
                }else{
                    return sum;
                }
                res = (abs(sum-target)<(abs(res-target)))? sum:res;
            }
        }
        
        return res;
    }
};
