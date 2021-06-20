class Solution {
    vector<string> ans;
    int given;
public:
    void makeParenthesis(int o_counts, int c_counts, string cur){
        if(o_counts < c_counts || o_counts > given){
            return;
        }
        if(c_counts == given){
            ans.push_back(cur);
            return;
        }
        makeParenthesis(o_counts+1, c_counts, cur+"(");
        makeParenthesis(o_counts, c_counts+1, cur+")");
        return;
    }
    vector<string> generateParenthesis(int n) {
        given= n;
        makeParenthesis(1, 0, "(");
        return ans;
    }
};
