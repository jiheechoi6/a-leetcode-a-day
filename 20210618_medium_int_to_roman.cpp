
class Solution {
public:
    map<int, string> roman = {{1, "I"}, {4, "IV"}, {5, "V"}, {9, "IV"}, {10, "X"}, {40, "XL"}, {50, "L"}, {90, "XC"}, {100, "C"}, {400, "CD"}, {500, "D"}, {900, "CM"}, {1000, "M"}};
    string intToRoman(int num) {
        string answer = "";
        int dec = 10;
        while(num >0){
            int digit = num%dec;
            num = num-digit;
            string digit_str = "";
            
            if((digit*10/dec)==4 || (digit*10/dec)==9){
                dec_str = roman[dec/10];
                digit += dec/10;
            }
            
            dec *=10;
            while(digit != 0){
                while(digit/1000>0){
                    digit_str = digit_str + roman[1000];
                    digit -= 1000;
                }
                while(digit/500>0){
                    digit_str = digit_str + roman[500];
                    digit -= 500;
                }
                while(digit/100>0){
                    digit_str = digit_str + roman[100];
                    digit -= 100;
                }
                while(digit/50>0){
                    digit_str = digit_str + roman[50];
                    digit -= 50;
                }
                while(digit/10){
                    digit_str = digit_str + roman[10];
                    digit -= 10;
                }
                while(digit/5){
                    digit_str = digit_str + roman[5];
                    digit -= 5;
                }
                while(digit/1){
                    digit_str = digit_str + roman[1];
                    digit -= 1;
                }
                answer = digit_str + answer;
            }
        }
        return answer;
    }
};
