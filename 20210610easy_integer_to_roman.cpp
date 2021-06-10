#include <map>
class Solution {
public:
    int romanToInt(string s) {
        int answer= 0;
        int prev = 1001;
        map<char, int> map = {{'M', 1000}, {'D', 500}, {'C', 100}, {'L', 50}, {'X', 10}, {'V', 5}, {'I', 1}};
        
        for(char&c: s){
            int cur = map[c];
            if(prev < cur){
                answer -= 2*prev;
            }
            
            answer += cur;
            prev = cur;
        }
        return answer;
    }
};
