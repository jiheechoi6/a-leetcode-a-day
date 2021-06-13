class Solution {
    vector<vector<int>> answer;
public:
    void permutate(vector<int> current, vector<int> nums){
        if(nums.size()==1){ // one left
            current.push_back(nums[0]);
            answer.push_back(current);
            return;
        }
        
        for(int i=0; i<nums.size(); i++){
            int temp = nums[0];
            nums.erase(nums.begin());
            current.push_back(temp);
            
            permutate(current, nums);
            
            nums.push_back(temp);
            current.pop_back();
        }
        return;
    }
    
    vector<vector<int>> permute(vector<int>& nums) {
        permutate({}, nums);
        
        return answer;
    }
};
