class Solution {
    std::map<int, std::vector<std::string>> dict={{'2', {"a", "b", "c"}},
                                                 {'3', {"d", "e", "f"}}, 
                                                 {'4', {"g", "h", "i"}},
                                                 {'5', {"j", "k", "l"}},
                                                 {'6', {"m", "n", "o"}},
                                                 {'7', {"p", "q", "r", "s"}},
                                                 {'8', {"t", "u", "v"}},
                                                 {'9', {"w", "x", "y", "z"}}};
    std::vector<string> answer;
    
public:
    void generateComb(string digits, string current, int start){
        if(start == digits.length()){
            answer.push_back(current);
        }
        
        for(string add: dict[digits[start]]){
            string new_cur = current + add;
            generateComb(digits, new_cur, start+1);
            new_cur.pop_back();
        }
    }
    
    vector<string> letterCombinations(string digits) {
        if(digits.length() == 0)    return answer;
        generateComb(digits, "", 0);
        return answer;
    }
};
