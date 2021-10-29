class Solution {
public:
    int largestRectangleArea(vector<int>& height) {
        height.push_back(0);
        stack<int> stk;
        stk.push(0);
        int i=1, maxa = 0;
        while(i<height.size()){
            if(stk.empty() || height[i]>=height[stk.top()]){
                stk.push(i++);
            }else{
                int h = height[stk.top()];
                stk.pop();
                maxa = max(maxa, h*(stk.empty()? i: i-stk.top()-1));
            }
        }
        
        return maxa;

    }
};
