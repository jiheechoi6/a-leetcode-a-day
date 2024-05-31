class Solution {
    public int climbStairs(int n) {
        if(n == 1) return 1;
        if(n == 2) return 2;
        int i1 = 1, i2 = 2, stair = 3;

        while(stair <= n){
            int temp = i2;
            i2 = i1 + i2;
            i1 = temp;
            stair++;
        }
        
        return i2;
    }
}
