class Solution {
public:
    vector<vector<int>> fourSum(vector<int>& nums, int target) {
        int len = nums.size();
        sort(nums.begin(), nums.end());
        vector<vector<int>> ans;
        int first, second, left, right;
        
        if(len < 4){
            return ans;
        }
        
        for(int i=0; i<len; i++){
            first = nums[i];
            
            if(i!=0 && first==nums[i-1])    continue;
            for(int j=i+1; j<len; j++){
                if(j!=i+1 && nums[j]==nums[j-1])    continue;
                left = j+1;
                right = len-1;
                
                while(left<right){
                    int four_sum = nums[i] + nums[j] + nums[left] + nums[right];
                
                    if(four_sum < target){
                        left++;
                    }else if(four_sum > target){
                        right--;
                    }else{
                        vector<int> new_elem = {nums[i], nums[j], nums[left], nums[right]};
                        ans.push_back(new_elem);

                        left++;
                        right--;
                        while(nums[left]==nums[left-1] && left<right){
                            left++;
                        }
                        while(left<right && nums[right]==nums[right+1]){
                            right--;
                        }    
                    }
                }
            }
        }
        return ans;
    }
};
