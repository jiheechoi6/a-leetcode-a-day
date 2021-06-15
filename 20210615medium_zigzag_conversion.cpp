class Solution {
public:
    string convert(string s, int numRows) {
        if(numRows == 1) return s;
        
        int row = 0;
        string answer = "";
        int cursor = 0;
        int big_diff = 2*(numRows-1);
        int str_len = s.length();
        bool even_col = true;
        
        for(int i=0; i< str_len; i++){
            if(row == 0 || row == numRows-1){
                answer += s[cursor];
                cursor += big_diff;
            }else{
                int dif;
                if(even_col){
                    dif = big_diff-2*row;
                    even_col = false;
                }else{
                    dif = row*2;
                    even_col = true;
                }
                answer += s[cursor];
                cursor += dif;
            }
            if(cursor >=str_len){
                row += 1;
                cursor = row;
                even_col = true;
            }
        }
        
        return answer;
    }
};
