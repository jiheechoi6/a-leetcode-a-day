#include <unordered_map>
class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        unordered_map<char, int> map;
        int index = 0;
        int max_len = 0;
        int last = -1;  // last index without repetition
        
        for(char& c: s){
            if(map.find(c) != map.end()){  // repetition found
                if(map[c]> last){
                    last = map[c];
                }
            }
            int now = index-last;
            if(now >max_len){
                max_len = now;
            }
            map[c] = index;
            index++;
        }
        
        return max_len;
    }
};
