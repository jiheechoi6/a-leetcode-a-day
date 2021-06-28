class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        int i = 0;
        int left;
        int right;
        int last_ind = nums.size()-1;
        vector<vector<int>> ans;
        
        sort(nums.begin(), nums.end());
        
        for(int num: nums){
            if(i != 0 && nums[i-1] == num){
                i++;
                continue;
            }
            left = i+1;
            right = last_ind;
            while(right>left){
                int three_some = num + nums[left] + nums[right];
                if(three_some < 0){
                    left++;
                }else if(three_some > 0){
                    right--;
                }else{
                    vector<int> new_elem = {num, nums[left], nums[right]};
                    ans.push_back(new_elem);
                    left++;
                    while((nums[left] == nums[left-1]) && left<right){
                        left++;
                    }
                }
            }
            i++;
        }
        return ans;
    }
};
