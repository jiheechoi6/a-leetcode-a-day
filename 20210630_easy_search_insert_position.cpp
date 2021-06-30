class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        int low = 0;
        int high = nums.size() - 1;
        int mid;
        
        while(low < high){
            mid = (high+low)/2;
            cout << "low: " << low << endl;
            cout << "high: " << high << endl;
            cout << "mid: " << mid << endl;
            int mid_num = nums[mid];
            
            if(low==high){
                return mid;
            }else if(mid_num == target){
                return mid;
            }else if(mid_num > target){
                high = mid-1;
            }else{
                low = mid+1;
            }
            
            cout << "low: " << low << endl;
            cout << "high: " << high << endl;
            cout << "mid: " << mid << endl;
        }
        return mid+1;
    }
};
