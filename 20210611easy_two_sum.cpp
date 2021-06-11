#include <map>

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> result{0,0};
        std::map<int, int> map;
        
        for(int i=0; i< nums.size(); i++){
            int cur = nums[i];
            int rest = target - cur;
            std::map<int, int>::iterator it = map.find(rest);
            if(it != map.end()){
                result[0] = i;
                result[1] = it->second;
                return result;
            }else{
                map[cur]= i;
            }
        }

        return result;
    }
};
