class Solution {
public:
    bool isValid(string s) {
        stack<char> st;
        map<char, char> m = {{'(', ')'}, {'[', ']'}, {'{', '}'}};
        
        for(char c: s){
            if(c=='(' || c=='{' || c=='['){
                st.push(m[c]);
            } else{
                if(st.empty())  return false;
                char top = st.top();
                st.pop();
                if(top != c)    return false;
            }
        }
        if(!st.empty()){
            return false;
        }
        return true;
    }
};
