class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        int low = 0;
        int high = nums.size() - 1;
        int mid = 0;
        
        if(target > nums[high]){
            return high+1;
        }
        
        while(low < high){
            mid = (high+low)/2;
            
            if(nums[mid] >= target){
                high = mid;
            }else{
                low = mid+1;
                mid++;
            }
        }
        return mid;
    }
};
