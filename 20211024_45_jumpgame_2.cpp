class Solution {
public:
    int jump(vector<int>& nums) {
        int start=0, end=0, step = 0;
        
        while(end < nums.size()-1){
            step++;
            int mx = start;
            for(int i=start; i<=end; i++){
                mx = max(mx, i + nums[i]);
            }
            start = end+1;
            end = mx;
        }
        return step;
    }
};
